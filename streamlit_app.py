import streamlit as st
import pandas as pd
import joblib
import requests
import io

# Function to load the model from a URL
def load_model_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        model = joblib.load(io.BytesIO(response.content))
        return model
    else:
        st.error("Failed to load model. Status code: {}".format(response.status_code))
        st.stop()

# URL of the model file
model_url = "https://raw.githubusercontent.com/mrIbadan/Alex-Optimisation-Demo/main/best_model.pkl"

# Load the model
model = load_model_from_url(model_url)

# Streamlit application code
st.title("🏡 Home Insurance Premium Predictor")

# User inputs
num_bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, value=3)
occupation = st.selectbox('Occupation', ['Unemployed', 'Employed', 'Self-employed'])
marital_status = st.selectbox('Marital Status', ['Single', 'Married'])
region = st.selectbox('Region', ['Region 0', 'Region 1', 'Region 2', 'Region 3'])
home_value = st.number_input('Home Value (£)', min_value=100000, max_value=500000, value=250000)
coverage_options = st.selectbox('Coverage Options', ['Option 0', 'Option 1', 'Option 2'])

# Prepare input for prediction
input_data = pd.DataFrame({
    'num_bedrooms': [num_bedrooms],
    'occupation': [occupation],
    'marital_status': [marital_status],
    'region': [region],
    'home_value': [home_value],
    'coverage_options': [coverage_options],
})

# One-hot encode the input
input_data = pd.get_dummies(input_data, drop_first=True)

# Ensure all model features are included
for column in model.feature_names_in_:
    if column not in input_data.columns:
        input_data[column] = 0

input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)

# Predict and display the result
if st.button('Get Quote'):
    price_prediction = model.predict(input_data)[0]
    st.success(f'Estimated Insurance Price: £{price_prediction:.2f}')
