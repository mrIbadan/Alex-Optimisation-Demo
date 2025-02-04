# Second Tab: Actual vs Expected
with tabs[1]:
    st.header('Actual vs Expected Model')

    model = load_model()  # Load model

    # Preprocess the data
    df_encoded = pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True)

    # Check the model's expected feature names
    expected_features = model.feature_name_

    # Align features with the model's expected features
    features = df_encoded.reindex(columns=expected_features, fill_value=0)

    # Make predictions for the whole dataset
    all_predictions = model.predict(features)

    # Prepare data for the chart
    df['Expected'] = all_predictions

    # Group by Exposure and calculate means for Actual and Expected
    exposure_summary = df.groupby("Exposure_EscapeOfWater").agg(
        Actual=('CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd', 'mean'),
        Expected=('Expected', 'mean'),
        Count=('CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd', 'count')  # Number of quotes
    ).reset_index()

    # Plotly chart with bars for actual values and lines for expected values
    fig = go.Figure()

    # Actual values as bars
    fig.add_trace(go.Bar(
        x=exposure_summary["Exposure_EscapeOfWater"],
        y=exposure_summary["Actual"],
        name='Actual',
        marker_color='blue',
        width=0.4,
        opacity=0.6
    ))

    # Expected values as a line
    fig.add_trace(go.Scatter(
        x=exposure_summary["Exposure_EscapeOfWater"],
        y=exposure_summary['Expected'],
        name='Expected',
        mode='lines+markers',
        line=dict(color='red', width=2),
        marker=dict(size=8)
    ))

    # Update layout for the chart
    fig.update_layout(
        title='Actual vs Expected by Exposure',
        xaxis_title='Exposure',
        yaxis_title='Values',
        width=1500,
        height=800,
        template='plotly_white'
    )

    # Show the plot
    st.plotly_chart(fig, use_container_width=True)

    # Calculate Mean Squared Error
    X_train, X_test, y_train, y_test = train_test_split(features, df['CalculatedResult_NetPremiumDiffFromPredictedMarketPremiumAmt_bnd'], test_size=0.2, random_state=42)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    st.write(f'Mean Squared Error: {mse:.2f}')
