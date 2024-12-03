import streamlit as st
import pandas as pd
import joblib
import requests
import os

# Function to download the model from GitHub
def download_model():
    url = "https://github.com/mrIbadan/Alex-Optimisation-Demo/raw/main/best_model.pkl"
    response = requests.get(url)
    
    # Save the model file
    with open('best_model.pkl', 'wb') as f:
        f.write(response.content)

# Check if the model file exists; if not, download it
if not os.path.exists('best_model.pkl'):
    download_model()

# Load the model
model = joblib.load('best_model.pkl')

# Function for making predictions
def predict_price(input_data):
    input_df = pd.DataFrame(input_data)
    input_df = pd.get_dummies(input_df, drop_first=True)
    prediction = model.predict(input_df)
    return prediction

# Streamlit UI
st.title("Home Insurance Price Prediction")

# User input
num_bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=5, value=3)
occupation = st.selectbox("Occupation", options=[0, 1, 2])
marital_status = st.selectbox("Marital Status", options=[0, 1])
region = st.selectbox("Region", options=[
    'North East', 'North West', 'Yorkshire and the Humber', 
    'East Midlands', 'West Midlands', 'East of England', 
    'London', 'South East', 'South West', 'Wales', 
    'Scotland', 'Northern Ireland'])
home_value = st.number_input("Home Value", min_value=100000, max_value=500000, value=300000)
coverage_options = st.selectbox("Coverage Options", options=['Bronze', 'Silver', 'Gold'])
num_bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=3, value=2)
garden_size = st.selectbox("Garden Size (0: No, 1: Yes)", options=[0, 1])

# Collecting input data
input_data = {
    "num_bedrooms": [num_bedrooms],
    "occupation": [occupation],
    "marital_status": [marital_status],
    "region": [region],
    "home_value": [home_value],
    "coverage_options": [coverage_options],
    "num_bathrooms": [num_bathrooms],
    "garden_size": [garden_size],
}

# Predict Button
if st.button("Predict"):
    prediction = predict_price(input_data)
    st.write(f"Predicted Insurance Price: ${prediction[0]:,.2f}")
