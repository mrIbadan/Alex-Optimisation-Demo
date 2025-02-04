import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
import plotly.graph_objects as go
import shap

# Load the model from GitHub
@st.cache_resource
def load_model():
    url = "https://github.com/mrIbadan/Alex-Optimisation-Demo/raw/main/home_insurance_model.pkl"
    response = requests.get(url)
    response.raise_for_status()
    model = pickle.loads(response.content)
    return model

# Generate synthetic data
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

# Display the logo
def display_logo():
    st.image("https://raw.githubusercontent.com/mrIbadan/Alex-Optimisation-Demo/main/Integra-Logo.jpg", width=150)

# Load data
df = generate_data()

# Load model
model = load_model()

# Streamlit app
st.sidebar.title("Navigation")
display_logo()

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
        df_modified = df.copy()
        if change_type == 'Price':
            df_modified[selected_factor] += change_value
        else:
            df_modified[selected_factor] *= (1 + change_value / 100)

        df_encoded = pd.get_dummies(df_modified, columns=["Occupation_v4", "Region_bnd"], drop_first=True)
        features = df_encoded.reindex(columns=model.feature_name_, fill_value=0)
        df_modified['Expected'] = model.predict(features)
        
        expected_loss_ratio = (df_modified['Expected'].sum() / df_modified['CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd'].sum()) * 100
        st.metric(label="Expected Loss Ratio", value=f"{expected_loss_ratio:.2f}%")
        st.success(f'Successfully changed {selected_factor} by {change_value} {change_type}')

# Second Tab: Actual vs Expected
with tabs[1]:
    st.header('Actual vs Expected Model')
    exposure_summary = df.groupby("Exposure_EscapeOfWater").agg(
        Actual=('CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd', 'mean'),
        Expected=('Expected', 'mean')
    ).reset_index()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=exposure_summary["Exposure_EscapeOfWater"], y=exposure_summary["Actual"], name='Actual', marker_color='blue', opacity=0.6))
    fig.add_trace(go.Scatter(x=exposure_summary["Exposure_EscapeOfWater"], y=exposure_summary['Expected'], name='Expected', mode='lines+markers', line=dict(color='red', width=2)))
    fig.update_layout(title='Actual vs Expected by Exposure', xaxis_title='Exposure', yaxis_title='Values', template='plotly_white')
    st.plotly_chart(fig, use_container_width=True)

# Third Tab: Shapley Values
with tabs[2]:
    st.header('Shapley Values Analysis')
    df_encoded = pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True)
    features = df_encoded.reindex(columns=model.feature_name_, fill_value=0)
    explainer = shap.Explainer(model)
    shap_values = explainer(features)
    st.subheader("SHAP Summary Plot")
    shap.summary_plot(shap_values, features, plot_type="bar", show=False)
    st.pyplot()
