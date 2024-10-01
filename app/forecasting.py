from statsmodels.tsa.arima.model import ARIMA

def predict_weather(data):
    """Train a simple ARIMA model to forecast future temperature."""
    # Using date_time as the index
    data.set_index('date_time', inplace=True)

    # Only using temperature for simplicity
    temperature_data = data['temperature']

    # Fit an ARIMA model (you can adjust the parameters (p,d,q))
    model = ARIMA(temperature_data, order=(5, 1, 0))
    model_fit = model.fit()

    # Forecast the next 7 days
    forecast = model_fit.forecast(steps=7)
    print("Weather forecast for the next 7 days (Temperature):")
    print(forecast)

    # Return predictions
    return forecast

if __name__ == "__main__":
    # Ensure to include the correct path to your data
    data = pd.read_csv('../data/current_weather_data.csv')
    forecast = predict_weather(data)
