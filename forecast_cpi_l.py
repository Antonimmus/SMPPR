# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the cleaned dataset
df = pd.read_csv('cleaned_data.csv')

# Ensure proper datetime formatting
df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str) + '-01')

# Define relevant categories for forecasting
relevant_categories = [
    'Cereals and products', 'Meat and fish', 'Egg', 'Milk and products',
    'Oils and fats', 'Fruits', 'Vegetables', 'Pulses and products',
    'Sugar and Confectionery', 'Spices', 'Non-alcoholic beverages',
    'Prepared meals, snacks, sweets etc.', 'Food and beverages',
    'Pan, tobacco and intoxicants', 'Clothing', 'Footwear',
    'Clothing and footwear', 'Fuel and light',
    'Household goods and services', 'Health',
    'Transport and communication', 'Recreation and amusement',
    'Education', 'Personal care and effects', 'Miscellaneous', 'General index'
]

# Streamlit app title and user inputs
st.markdown("<h2 style='text-align: center;'>LSTM Time Series Forecasting</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    sector = st.selectbox('Select Sector', df['Sector'].unique())
with col2:
    category = st.selectbox('Select Category', relevant_categories)

n_periods = st.slider('Select number of months to forecast (1-120)', 1, 120)

# Filter data based on user input
filtered_data = df[df['Sector'] == sector]
time_series = filtered_data[['Date', category]].set_index('Date').asfreq('MS')[category].dropna()

# Function to prepare data for LSTM
def prepare_data(data, n_steps):
    X, y = [], []
    for i in range(len(data) - n_steps):
        X.append(data[i:i + n_steps])
        y.append(data[i + n_steps])
    return np.array(X), np.array(y)

# Check for LSTM forecast update
if st.checkbox('Update LSTM Forecast', value=True):
    # Scale the data
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(time_series.values.reshape(-1, 1))

    # Prepare dataset
    n_steps = 5
    X, y = prepare_data(scaled_data, n_steps)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Build LSTM model
    model = Sequential([
        LSTM(50, activation='relu', input_shape=(X.shape[1], 1)),
        Dropout(0.2),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, y, epochs=50, verbose=0)

    # Make predictions
    forecast_lstm = []
    last_data = scaled_data[-n_steps:]

    for _ in range(n_periods):
        input_data = last_data.reshape((1, n_steps, 1))
        prediction = model.predict(input_data, verbose=0)
        forecast_lstm.append(prediction[0, 0])
        last_data = np.append(last_data[1:], prediction)

    # Inverse transform predictions
    forecast_lstm = scaler.inverse_transform(np.array(forecast_lstm).reshape(-1, 1))

    # Create future dates for the forecast
    future_dates_lstm = pd.date_range(start=time_series.index[-1], periods=n_periods + 1, freq='MS')[1:]

    # Plot results
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time_series.index, y=time_series, mode='lines', name='Actual', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=future_dates_lstm, y=forecast_lstm.flatten(), mode='lines', name='Predicted', line=dict(color='orange')))
    fig.update_layout(
        title=f"LSTM Forecast for {category} in {sector} Sector",
        xaxis_title='Date',
        yaxis_title=category,
        legend=dict(x=0, y=1)
    )
    st.plotly_chart(fig)

    # Evaluate model performance
    if len(forecast_lstm) == n_periods:
        mae = mean_absolute_error(time_series[-n_periods:], forecast_lstm.flatten())
        rmse = mean_squared_error(time_series[-n_periods:], forecast_lstm.flatten(), squared=False)

        st.write(f"**Mean Absolute Error (MAE):** {mae:.4f}")
        st.write(f"**Root Mean Squared Error (RMSE):** {rmse:.4f}")
