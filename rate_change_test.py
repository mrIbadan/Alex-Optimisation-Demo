import streamlit as st
import pandas as pd
import numpy as np
import lightgbm as lgb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

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

    # Prepare data for bar chart
    exposure_summary = df.groupby("Exposure_EscapeOfWater")["CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd"].mean().reset_index()

    # Plotting bar chart for Exposure
    plt.figure(figsize=(12, 6))
    plt.bar(exposure_summary["Exposure_EscapeOfWater"], exposure_summary["CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd"], color='skyblue')
    plt.xlabel('Exposure (Number of Quotes for Escape of Water)')
    plt.ylabel('Average Net Premium Difference')
    plt.title('Average Net Premium Difference by Exposure')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    st.pyplot(plt)

    # Display metrics
    mse = mean_squared_error(y_test, y_pred)
    st.write(f'Mean Squared Error: {mse:.2f}')
