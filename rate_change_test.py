import streamlit as st
import pandas as pd
import numpy as np
import lightgbm as lgb
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.graph_objects as go
import shap

# Load the model from the URL
@st.cache_resource
def load_model():
    url = "https://github.com/mrIbadan/Alex-Optimisation-Demo/raw/main/home_insurance_model.pkl"
    response = requests.get(url)
    with open("home_insurance_model.pkl", "wb") as f:
        f.write(response.content)
    with open("home_insurance_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

# Generate synthetic data
def generate_data(n_rows=10000):
    np.random.seed(42)
    data = {
        "Exposure_EscapeOfWater": np.random.randint(1, 100, n_rows),
        "ArSpecifiedItems_AmtReqd_bnd": np.random.randint(0, 10, n_rows),
        "ArUnspecifiedItems_AmtReqd_bnd": np.random.randint(0, 10, n_rows),
        "BuildingsCover_AccidentalDamageGrantedInd_bnd": np.random.randint(0, 2, n_rows),
        "BuildingsCover_VolXsGranted_bnd": np.random.randint(0, 5, n_rows),
        "CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd": np.random.uniform(0, 100, n_rows),
        "Occupation_v4": np.random.choice(["Professional", "Manual", "Retired", "Student"], n_rows),
        "Region_bnd": np.random.choice(["North", "South", "East", "West"], n_rows),
    }
    return pd.DataFrame(data)

# Load data
df = generate_data()

# Streamlit app
st.image("https://raw.githubusercontent.com/mrIbadan/Alex-Optimisation-Demo/main/Integra-Logo.jpg", width=150)
st.markdown("<h1 style='text-align: left;'>Insurance Home Claims Model</h1>", unsafe_allow_html=True)

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
        st.success(f'Successfully changed {selected_factor} by {change_value} {change_type}')

# Second Tab: Actual vs Expected
with tabs[1]:
    st.header('Actual vs Expected Model')

    model = load_model()  # Load model

    # Preprocess the data
    df_encoded = pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True)
    features = df_encoded.drop(columns=["CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd"])
    target = df_encoded["CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd"]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Make predictions
    y_pred = model.predict(X_test)

    # Prepare data for the chart
    exposure_summary = df_encoded.groupby("Exposure_EscapeOfWater").agg(
        Actual=('CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd', 'mean'),
        Expected=('CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd', 'mean')  # Placeholder
    ).reset_index()

    # Use predictions for Expected
    exposure_summary['Expected'] = model.predict(features.groupby("Exposure_EscapeOfWater").mean().reset_index())

    # Plotly chart
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=exposure_summary["Exposure_EscapeOfWater"],
        y=exposure_summary["Actual"],
        name='Actual',
        marker_color='blue',
        width=0.9  # Wider bars
    ))
    fig.add_trace(go.Scatter(
        x=exposure_summary["Exposure_EscapeOfWater"],
        y=exposure_summary["Expected"],
        name='Expected',
        mode='lines+markers',
        line=dict(color='red', width=4),
        marker=dict(size=10)
    ))

    fig.update_layout(
        title='Actual vs Expected by Exposure',
        xaxis_title='Exposure',
        yaxis_title='Values',
        width=1500, height=800,
        template='plotly_white'
    )

    fig.update_yaxes(range=[0, max(exposure_summary["Actual"].max(), exposure_summary["Expected"].max()) * 1.5])
    st.plotly_chart(fig, use_container_width=True)

    mse = mean_squared_error(y_test, y_pred)
    st.write(f'Mean Squared Error: {mse:.2f}')

# Third Tab: Shapley Values
with tabs[2]:
    st.header('Shapley Values Analysis')

    model = load_model()  # Load the model again for Shapley values
    df_encoded = pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True)
    features = df_encoded.drop(columns=["CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd"])

    # Calculate Shapley values
    explainer = shap.Explainer(model)
    shap_values = explainer(features)

    # Plot SHAP summary
    st.subheader("SHAP Summary Plot")
    shap.summary_plot(shap_values, features, plot_type="bar", show=False)
    st.pyplot()  # Render the SHAP plot
