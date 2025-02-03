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
        "CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd": np.random.uniform(0, 100, n_rows),  # No negative values
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

    # Scale the data for better visualization
    exposure_summary["Actual"] *= 10  # Scale Actual values for more variation
    exposure_summary["Expected"] *= 5  # Scale Expected values for more variation

    # Plotly chart
    fig = go.Figure()

    # Adding bars for Actual values in blue
    fig.add_trace(go.Bar(
        x=exposure_summary["Exposure_EscapeOfWater"],
        y=exposure_summary["Actual"],
        name='Actual',
        marker_color='blue',
        width=0.8  # Wider bars
    ))

    # Adding line for Expected values in red on a secondary y-axis
    fig.add_trace(go.Scatter(
        x=exposure_summary["Exposure_EscapeOfWater"],
        y=exposure_summary["Expected"],
        name='Expected',
        mode='lines+markers',
        line=dict(color='red', width=3),  # Thicker line
        marker=dict(size=10),
        yaxis='y2'  # Assign to secondary y-axis
    ))

    # Update layout
    fig.update_layout(
        title='Actual vs Expected by Exposure',
        xaxis_title='Exposure (Number of Quotes for Escape of Water)',
        yaxis_title='Actual Values',
        yaxis=dict(
            rangemode='tozero',  # Start y-axis from 0
            title='Actual Values'
        ),
        yaxis2=dict(
            title='Expected Values',
            overlaying='y',
            side='right',
            showgrid=False,  # Hide grid for secondary y-axis
            rangemode='tozero'  # Start secondary y-axis from 0
        ),
        legend_title='Legend',
        width=1400,  # Wider chart
        height=900,  # Taller chart
        template='plotly_white'
    )

    # Set Y-axis range starting from 0
    fig.update_yaxes(range=[0, max(exposure_summary["Actual"].max(), exposure_summary["Expected"].max()) * 1.1])  # 10%
