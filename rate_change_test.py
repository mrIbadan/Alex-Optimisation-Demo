import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import roc_curve, auc
import joblib
import shap  # For SHAP values

# Generate synthetic data
def generate_data(rows=10000):
    data = {
        'Escape_Of_Water': np.random.randint(1000, 5000, size=rows),
        'ArSpecifiedItems_AmtReqd_bnd': np.random.randint(1000, 5000, size=rows),
        'ArUnspecifiedItems_AmtReqd_bnd': np.random.randint(1000, 5000, size=rows),
        'BuildingsCover_AccidentalDamageGrantedInd_bnd': np.random.choice([0, 1], size=rows),
        'CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd': np.random.uniform(-1000, 1000, size=rows),
        'Premises_NoBedrooms_bnd': np.random.randint(1, 6, size=rows),
        'Region_bnd': np.random.choice(['North', 'South', 'East', 'West'], size=rows),
    }
    return pd.DataFrame(data)

data = generate_data()

# Preprocess categorical variables
def preprocess_data(df):
    return pd.get_dummies(df, drop_first=True)

data = preprocess_data(data)

# Streamlit app
st.title('Insurance Home Claims Model')

# Function to display error messages
def display_error(error_message):
    st.error(f"Error: {error_message}")

# Tabs for the application
tabs = st.tabs(['Rate Change', 'Exposure Analysis', 'Statistical Reports', 'Model Benchmarking', 'ROC Curve', 'SHAP Values'])

# First Tab: Rate Change
with tabs[0]:
    st.header('Rate Change Interface')
    try:
        selected_factor = st.selectbox('Select Factor to Change', data.columns)
        change_type = st.radio('Change Type', ('Price', 'Percentage'))
        change_value = st.number_input('Enter Change Value', value=0.0)

        if st.button('Apply Change'):
            if change_type == 'Price':
                data[selected_factor] += change_value
            else:
                data[selected_factor] *= (1 + change_value / 100)
            st.success(f'Successfully changed {selected_factor} by {change_value} {change_type}')
    except Exception as e:
        display_error(e)

# Second Tab: Exposure Analysis
with tabs[1]:
    st.header('Exposure Analysis')
    try:
        exposure = data.groupby(['Premises_NoBedrooms_bnd']).size().reset_index(name='Count')
        avg_premium = data.groupby(['Premises_NoBedrooms_bnd'])['CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd'].mean().reset_index(name='Average Premium')

        merged_data = pd.merge(exposure, avg_premium, on='Premises_NoBedrooms_bnd')

        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()

        sns.barplot(x='Premises_NoBedrooms_bnd', y='Count', data=merged_data, ax=ax1, color='g', alpha=0.6)
        sns.lineplot(x='Premises_NoBedrooms_bnd', y='Average Premium', data=merged_data, ax=ax2, color='b')

        ax1.set_xlabel('Number of Bedrooms')
        ax1.set_ylabel('Count of Quotes', color='g')
        ax2.set_ylabel('Average Premium', color='b')

        st.pyplot(fig)
    except Exception as e:
        display_error(e)

# Third Tab: Statistical Reports
with tabs[2]:
    st.header('Statistical Reports')
    try:
        st.write(data.describe())
    except Exception as e:
        display_error(e)

# Fourth Tab: Model Benchmarking
with tabs[3]:
    st.header('Model Benchmarking')
    try:
        features = data.drop(columns=['CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd'])
        target = data['CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd']

        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        models = {
            'GLM': LinearRegression(),
            'XGBoost': XGBRegressor(),
            'LightGBM': LGBMRegressor(),
            'CatBoost': CatBoostRegressor(silent=True),
        }

        # Train and save models
        for name, model in models.items():
            model.fit(X_train, y_train)
            joblib.dump(model, f'{name}.pkl')  # Save model as .pkl

        results = {name: model.score(X_test, y_test) for name, model in models.items()}
        st.bar_chart(results)
    except Exception as e:
        display_error(e)

# Fifth Tab: ROC Curve
with tabs[4]:
    st.header('ROC Curve for Best Model')
    try:
        best_model_name = st.selectbox('Select Best Model', list(models.keys()))

        # Load the selected model
        best_model = joblib.load(f'{best_model_name}.pkl')

        y_pred_proba = best_model.predict(X_test)
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
        roc_auc = auc(fpr, tpr)

        plt.figure()
        plt.plot(fpr, tpr, color='blue', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
        plt.plot([0, 1], [0, 1], color='red', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic')
        plt.legend(loc='lower right')
        st.pyplot()
    except Exception as e:
        display_error(e)

# Sixth Tab: SHAP Values
with tabs[5]:
    st.header('SHAP Values for Selected Model')
    try:
        best_model_name = st.selectbox('Select Best Model for SHAP', list(models.keys()))
        best_model = joblib.load(f'{best_model_name}.pkl')

        explainer = shap.Explainer(best_model, X_train)
        shap_values = explainer(X_test)

        st.subheader('SHAP Summary Plot')
        shap.summary_plot(shap_values, X_test, plot_type="bar")
        st.pyplot()
    except Exception as e:
        display_error(e)
