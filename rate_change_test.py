import subprocess
import sys
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import roc_curve, auc

def install_if_missing(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required packages
packages = ["pandas", "numpy", "matplotlib", "seaborn", "plotly", "scikit-learn", "xgboost", "lightgbm", "catboost", "streamlit"]
for package in packages:
    install_if_missing(package)

def generate_data(n=10000):
    np.random.seed(42)
    return pd.DataFrame({
        'Premises_NoBedrooms_bnd': np.random.choice([1, 2, 3, 4, 5], n),
        'ContentsCover_TotXsAmt_bnd': np.random.uniform(100, 1000, n),
        'PremiumUnperturbed_BO_bnd': np.random.uniform(200, 500, n),
        'PremiumUnperturbed_CO_bnd': np.random.uniform(250, 600, n),
        'Exposure': np.random.randint(50, 500, n),
        'Expected_Premium': np.random.uniform(300, 700, n),
        'Average_Premium': np.random.uniform(250, 650, n),
        'Target': np.random.choice([0, 1], n)
    })

data = generate_data()

st.title("Insurance Home Claims Model")
tabs = ["Rate Adjustment", "Exposure Analysis", "Statistical Reports", "Model Benchmarking", "ROC Curve"]
selected_tab = st.sidebar.radio("Select a tab", tabs)

if selected_tab == "Rate Adjustment":
    st.header("Rate Adjustment Tool")
    adjustment_type = st.radio("Choose Adjustment Type", ["Percentage", "Absolute"])
    adjustment_value = st.number_input("Enter Adjustment Value", value=0.0)
    factor = st.selectbox("Select Factor to Adjust", data.columns)
    
    if st.button("Apply Adjustment"):
        if adjustment_type == 'Percentage':
            data[factor] *= (1 + adjustment_value / 100)
        else:
            data[factor] += adjustment_value
        st.write(f"Applied {adjustment_type} adjustment of {adjustment_value} to {factor}")
        st.dataframe(data.head())

elif selected_tab == "Exposure Analysis":
    st.header("Exposure Analysis")
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data['Exposure'], y=data['Average_Premium'], name='Average Premium', marker_color='blue'))
    fig.add_trace(go.Scatter(x=data['Exposure'], y=data['Expected_Premium'], name='Expected Premium', mode='lines+markers', line=dict(color='red')))
    
    fig.update_layout(
        title="Exposure vs Premium",
        xaxis_title="Exposure",
        yaxis_title="Premium",
        legend_title="Legend",
        width=1200,
        height=800
    )
    st.plotly_chart(fig)

elif selected_tab == "Statistical Reports":
    st.header("Statistical Summary")
    st.write(data.describe())

elif selected_tab == "Model Benchmarking":
    st.header("Benchmarking Models")
    X = data[['Premises_NoBedrooms_bnd', 'ContentsCover_TotXsAmt_bnd']]
    y = data['PremiumUnperturbed_BO_bnd']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'Linear Regression': LinearRegression(),
        'XGBoost': XGBRegressor(),
        'LightGBM': LGBMRegressor(),
        'CatBoost': CatBoostRegressor(verbose=0)
    }

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        results[name] = model.score(X_test, y_test)
    
    fig, ax = plt.subplots()
    ax.bar(results.keys(), results.values())
    ax.set_ylabel("Model Score")
    ax.set_title("Model Performance Comparison")
    st.pyplot(fig)

elif selected_tab == "ROC Curve":
    st.header("ROC Curve Analysis")
    X = data[['Premises_NoBedrooms_bnd', 'ContentsCover_TotXsAmt_bnd']]
    y = data['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    best_model = XGBRegressor()
    best_model.fit(X_train, y_train)
    y_pred_prob = best_model.predict(X_test)
    fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
    roc_auc = auc(fpr, tpr)
    
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label=f'ROC curve (area = {roc_auc:.2f}')
    ax.plot([0, 1], [0, 1], 'k--')
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("Receiver Operating Characteristic")
    ax.legend()
    st.pyplot(fig)
