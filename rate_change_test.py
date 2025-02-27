import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
import plotly.graph_objects as go
import shap

# Load the model from the GitHub raw URL
@st.cache_resource
def load_model():
    url = "https://github.com/mrIbadan/Alex-Optimisation-Demo/raw/main/home_insurance_model.pkl"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    model = pickle.loads(response.content)
    return model

# Generate realistic synthetic data
def generate_data(n_rows=10000):
    np.random.seed(42)
    regions = [
        "Northern Ireland", "Scotland", "Wales", "East Midlands", 
        "East of England", "London", "North East", "North West", 
        "South East", "South West", "West Midlands", "Yorkshire and The Humber"
    ]
    
    data = {
        "Exposure_EscapeOfWater": np.random.normal(loc=50, scale=20, size=n_rows).clip(0, 100),
        "ArSpecifiedItems_AmtReqd_bnd": np.random.randint(0, 10, n_rows),
        "ArUnspecifiedItems_AmtReqd_bnd": np.random.randint(0, 10, n_rows),
        "BuildingsCover_AccidentalDamageGrantedInd_bnd": np.random.randint(0, 2, n_rows),
        "BuildingsCover_VolXsGranted_bnd": np.random.randint(0, 5, n_rows),
        "CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd": np.random.uniform(0, 100, n_rows),
        "Occupation_v4": np.random.choice(["Professional", "Manual", "Retired", "Student"], n_rows),
        "Region_bnd": np.random.choice(regions, n_rows),
    }
    return pd.DataFrame(data)

# Function to display the logo
def display_logo():
    st.image("https://raw.githubusercontent.com/mrIbadan/Alex-Optimisation-Demo/main/Integra-Logo.jpg", width=150)

# Load data
df = generate_data()

# Streamlit app
st.set_page_config(page_title="Insurance Home Claims Model", layout="wide")
display_logo()
st.markdown("<h1 style='text-align: left;'>Insurance Home Claims Model</h1>", unsafe_allow_html=True)

# Load model
model = load_model()

# Prepare initial expected values
df_encoded = pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True)
expected_features = model.feature_names_in_

# Ensure the dataframe has the correct features
df_encoded = df_encoded.reindex(columns=expected_features, fill_value=0)
df['Expected'] = model.predict(df_encoded)

# Tab layout
tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values'])

# First Tab: Rate Change
with tabs[0]:
    st.header('Rate Change Interface')
    
    selected_factor = st.selectbox('Select Factor to Change', df.columns)
    change_type = st.radio('Change Type', ('Price', 'Percentage'))
    change_value = st.number_input('Enter Change Value', value=0.0)

    if st.button('Apply Change'):
        if change_type == 'Price':
            df[selected_factor] += change_value
        else:
            df[selected_factor] *= (1 + change_value / 100)

        # Recalculate expected values after change
        df_encoded = pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True)
        df_encoded = df_encoded.reindex(columns=expected_features, fill_value=0)
        df['Expected'] = model.predict(df_encoded)

        # Calculate and display KPIs
        expected_loss_ratio = (df['Expected'].sum() / df['CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd'].sum()) * 100
        st.metric(label="Expected Loss Ratio", value=f"{expected_loss_ratio:.2f}%")
        st.success(f'Successfully changed {selected_factor} by {change_value} {change_type}')

# Second Tab: Actual vs Expected
with tabs[1]:
    st.header('Actual vs Expected Model')

    # Dropdown to select the factor for filtering
    selected_factor = st.selectbox('Select Factor to Analyze', df.columns)

    # Prepare data for the chart
    exposure_summary = df.groupby(selected_factor).agg(
        Actual=('CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd', 'mean'),
        Expected=('Expected', 'mean'),
        Count=('CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd', 'count')
    ).reset_index()

    # Create figure with secondary y-axis
    fig = go.Figure()

    # Add Actual values as bars (Y-axis 1)
    fig.add_trace(go.Bar(
        x=exposure_summary[selected_factor],
        y=exposure_summary["Actual"],
        name='Actual (Historic Data)',
        marker_color='green',
        width=0.5,  # Wider bars
        opacity=0.6,
        yaxis='y1'
    ))

    # Add Expected values as a line (Y-axis 2)
    fig.add_trace(go.Scatter(
        x=exposure_summary[selected_factor],
        y=exposure_summary['Expected'],
        name='Expected (Predicted)',
        mode='lines+markers',
        line=dict(color='red', width=4),  # Thicker line for visibility
        marker=dict(size=8),
        yaxis='y2'
    ))

    # Add Count of Quotes as bars (X-axis)
    fig.add_trace(go.Bar(
        x=exposure_summary[selected_factor],
        y=exposure_summary["Count"],
        name='Number of Quotes',
        marker_color='blue',
        width=0.5,  # Wider bars
        opacity=0.4,
        yaxis='y1'
    ))

    # Update layout for the chart
    fig.update_layout(
        title=f'Actual vs Expected by {selected_factor}',
        xaxis_title=selected_factor,
        yaxis=dict(
            title='Actual Values (Historic Data)',
            titlefont=dict(color='green'),
            tickfont=dict(color='green')
        ),
        yaxis2=dict(
            title='Expected Values (Predicted)',
            titlefont=dict(color='red'),
            tickfont=dict(color='red'),
            overlaying='y',
            side='right'
        ),
        width=1500,
        height=800,
        template='plotly_white',
        barmode='group'  # Group bars for better visibility
    )

    # Show the plot
    st.plotly_chart(fig, use_container_width=True)

# Third Tab: Shapley Values
with tabs[2]:
    st.header('Shapley Values Analysis')

    # Calculate Shapley values
    df_encoded = pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True)
    df_encoded = df_encoded.reindex(columns=expected_features, fill_value=0)

    explainer = shap.Explainer(model)
    shap_values = explainer(df_encoded)

    # Plot SHAP summary
    st.subheader("SHAP Summary Plot")
    shap.summary_plot(shap_values, df_encoded, plot_type="bar", show=False)
    st.pyplot()  # Render the SHAP plot
