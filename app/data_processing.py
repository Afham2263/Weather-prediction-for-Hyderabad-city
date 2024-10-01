import pandas as pd

def process_data(file_path):
    # Read the CSV file with no headers (header=None)
    data = pd.read_csv(file_path, header=None)

    # Define the column names explicitly
    data.columns = ['city', 'temperature', 'humidity', 'wind_speed', 'weather_description', 'date_time']

    # Print the DataFrame and its columns for debugging
    print("Data read from", file_path)
    print(data.head())  # Print the first few rows of the DataFrame
    print("Columns:", data.columns.tolist())  # Print the list of column names

    # Strip any leading/trailing spaces from column names
    data.columns = data.columns.str.strip()

    # Check if 'date_time' exists in columns
    if 'date_time' not in data.columns:
        print("Error: 'date_time' column not found.")
        return None

    # Optionally convert date_time to datetime type
    data['date_time'] = pd.to_datetime(data['date_time'], errors='coerce')

    # Handle missing data or clean the DataFrame as needed here
    data.dropna(subset=['date_time'], inplace=True)

    return data
