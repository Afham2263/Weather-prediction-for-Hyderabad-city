import pandas as pd
import matplotlib.pyplot as plt
from data_processing import process_data  # Ensure this import matches your directory structure
from statsmodels.tsa.arima.model import ARIMA


def forecast_temperature(data):
    # Fit an ARIMA model to the historical temperature data
    model = ARIMA(data['temperature'], order=(1, 1, 1))
    model_fit = model.fit()

    # Forecast the next 7 days
    forecast = model_fit.forecast(steps=7)
    return pd.Series(forecast, name='predicted_mean')


def visualize_data(data, predictions):
    # Create a date range for future dates
    future_dates = pd.date_range(start=data['date_time'].max(), periods=8, freq='D')[1:]

    plt.figure(figsize=(10, 5))
    plt.plot(data['date_time'], data['temperature'], label='Historical Temperature', marker='o')
    plt.plot(future_dates, predictions, label='Predicted Temperature', marker='x')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Weather Forecast')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()  # Adjust layout to prevent clipping
    plt.show()


def main():
    file_path = 'C:/Users/aqueel mohammed/Desktop/weatherPrediction/data/current_weather_data.csv'  # Ensure this path is correct
    processed_data = process_data(file_path)

    # Check if processed_data is None
    if processed_data is None or 'date_time' not in processed_data.columns:
        print("Exiting due to missing data.")
        return

    # Ensure 'date_time' is in datetime format
    processed_data['date_time'] = pd.to_datetime(processed_data['date_time'], errors='coerce')

    # Remove rows with NaT in 'date_time' after conversion
    processed_data.dropna(subset=['date_time'], inplace=True)

    # Forecast temperature
    predictions = forecast_temperature(processed_data)

    # Visualize the results
    visualize_data(processed_data, predictions)


if __name__ == "__main__":
    main()
