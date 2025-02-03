import streamlit as st
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.graph_objects as go

# Generate synthetic data
def generate_data(n_rows=10000):
    np.random.seed(42)
    data = {
        "Exposure_EscapeOfWater": np.random.randint(1, 100, n_rows),  # Exposure variable
        "ArSpecifiedItems_AmtReqd_bnd": np.random.randint(0, 10, n_rows),
        "ArUnspecifiedItems_AmtReqd_bnd": np.random.randint(0, 10, n_rows),
        "BuildingsCover_AccidentalDamageGrantedInd_bnd": np.random.randint(0, 2, n_rows),
        "BuildingsCover_VolXsGranted_bnd": np.random.randint(0, 5, n_rows),
        "CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd": np.random.uniform(-100, 100, n_rows),
        "Occupation_v4": np.random.choice(["Professional", "Manual", "Retired", "Student"], n_rows),
        "Region_bnd": np.random.choice(["North", "South", "East", "West"], n_rows),
    }
    return pd.DataFrame(data)

# Load data
df = generate_data()

# Streamlit app
st.image("https://raw.githubusercontent.com/mrIbadan/Alex-Optimisation-Demo/main/Integra-Logo.jpg", width=150)  # Logo URL
st.markdown("<h1 style='text-align: left;'>Insurance Home Claims Model</h1>", unsafe_allow_html=True)

# Tab layout
tabs = st.tabs(['Rate Change', 'Actual vs Expected'])

# First Tab: Rate Change
with tabs[0]:
    st.image("https://raw.githubusercontent.com/mrIbadan/Alex-Optimisation-Demo/main/Integra-Logo.jpg", width=150)  # Logo for Rate Change tab
    st.header('Rate Change Interface')
    selected_factor = st.selectbox('Select Factor to Change', df.columns)
    change_type = st.radio('Change Type', ('Price', 'Percentage'))
    change_value = st.number_input('Enter Change Value', value=0.0)

    if st.button('Apply Change'):
        if change_type == 'Price':
            df[selected_factor] += change_value
        else:
            df[selected_factor] *= (1 + change_value / 100)
        st.success(f'Successfully changed {selected_factor} by {change_value} {change_type}')

# Second Tab: Actual vs Expected
with tabs[1]:
    st.image("https://raw.githubusercontent.com/mrIbadan/Alex-Optimisation-Demo/main/Integra-Logo.jpg", width=150)  # Logo for Actual vs Expected tab
    st.header('Actual vs Expected Model')

    # Preprocess the data
    df_encoded = pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True)

    # Prepare data for modeling
    features = df_encoded.drop(columns=["CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd"])
    target = df_encoded["CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd"]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Train a LightGBM model
    model = lgb.LGBMRegressor()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Prepare data for the chart
    exposure_summary = df.groupby("Exposure_EscapeOfWater").agg(
        Actual=('CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd', 'mean'),
        Expected=('CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd', 'mean')  # Placeholder for expected values
    ).reset_index()

    # Plotly chart
    fig = go.Figure()

    # Adding bars for Exposure in blue
    fig.add_trace(go.Bar(
        x=exposure_summary["Exposure_EscapeOfWater"],
        y=exposure_summary["Actual"],
        name='Actual',
        marker_color='blue',  # Bars in blue
        width=0.5  # Wider bars
    ))

    # Adding line for Expected values in red
    fig.add_trace(go.Scatter(
        x=exposure_summary["Exposure_EscapeOfWater"],
        y=exposure_summary["Expected"],
        name='Expected',
        mode='lines+markers',
        line=dict(color='red', width=4),  # Thicker line for visibility
        marker=dict(size=10)
    ))

    # Update layout for full-sized chart and dual axes
    fig.update_layout(
        title='Actual vs Expected by Exposure',
        xaxis_title='Exposure (Number of Quotes for Escape of Water)',
        yaxis_title='Actual Values',
        legend_title='Legend',
        width=1500,  # Wider chart
        height=800,  # Adjust height for better visibility
        template='plotly_white'
    )
    
    # Set Y-axis range starting from 0 for Actual
    fig.update_yaxes(range=[0, exposure_summary["Actual"].max() * 1.5], title_text="Actual Values", secondary_y=False, title_font=dict(color="green"), tickfont=dict(color="green"))

    # Add second Y-axis for Expected values
    fig.add_trace(go.Scatter(
        x=exposure_summary["Exposure_EscapeOfWater"],
        y=exposure_summary["Expected"],
        name='Expected',
        mode='lines+markers',
        line=dict(color='red', width=4),
        marker=dict(size=10),
        yaxis='y2'
    ))

    # Set properties for the second Y-axis
    fig.update_layout(
        yaxis2=dict(
            title='Expected Values',
            overlaying='y',
            side='right',
            title_font=dict(color="red"),
            tickfont=dict(color="red"),
            range=[0, exposure_summary["Expected"].max() * 1.5]  # Adjust for better visibility
        )
    )

    # Display Plotly chart in full width
    st.plotly_chart(fig, use_container_width=True)

    # Display metrics
    mse = mean_squared_error(y_test, y_pred)
    st.write(f'Mean Squared Error: {mse:.2f}')
