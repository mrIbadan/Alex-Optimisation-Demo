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
        "ArSpecifiedItems_AmtReqd_bnd": np.random.randint(0, 10, n_rows),
        "ArUnspecifiedItems_AmtReqd_bnd": np.random.randint(0, 10, n_rows),
        "BuildingsCover_AccidentalDamageGrantedInd_bnd": np.random.randint(0, 2, n_rows),
        "BuildingsCover_VolXsGranted_bnd": np.random.randint(0, 5, n_rows),
        "CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd": np.random.uniform(-100, 100, n_rows),
        "CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumRel_bnd": np.random.uniform(-0.5, 0.5, n_rows),
        "CalculatedResult_NetPremiumExclIpt_BO_bnd": np.random.uniform(100, 1000, n_rows),
        "CalculatedResult_NetPremiumExclIpt_CO_bnd": np.random.uniform(100, 1000, n_rows),
        "CalculatedResult_NetPremiumExclIpt_JC_bnd": np.random.uniform(100, 1000, n_rows),
        "Occupation_v4": np.random.choice(["Professional", "Manual", "Retired", "Student"], n_rows),
        "Region_bnd": np.random.choice(["North", "South", "East", "West"], n_rows),
        "Renewal_PremiumChangeYoY_bnd": np.random.uniform(-0.2, 0.2, n_rows),
    }
    return pd.DataFrame(data)

# Load data
df = generate_data()

# Streamlit app
st.title("Insurance Home Claims Model")

# Tabs for the application
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

    # Prepare data for modeling
    features = df.drop(columns=["CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd"])
    target = df["CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd"]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Train a LightGBM model
    model = lgb.LGBMRegressor()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Plotting Actual vs Expected
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Index')
    ax1.set_ylabel('Actual', color='tab:blue')
    ax1.plot(y_test.values, label='Actual', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Expected', color='tab:red')  # we already handled the x-label with ax1
    ax2.plot(y_pred, label='Predicted', color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    st.pyplot(fig)

    # Display metrics
    mse = mean_squared_error(y_test, y_pred)
    st.write(f'Mean Squared Error: {mse:.2f}')
