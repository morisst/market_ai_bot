import pandas as pd

# Function to resample data
def resample_data(data, interval):
    # Convert the 'Timestamp' column to datetime
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Set the 'Timestamp' column as the index
    data.set_index('Timestamp', inplace=True)

    # Resample the data to the specified interval
    resampled_data = data.resample(f'{interval}T').agg({
        'Open': 'first',
        'Close': 'last',
        'High': 'max',
        'Low': 'min',
        'Volume': 'sum'
    })

    resampled_data.dropna(inplace=True)

    # Reset the index
    resampled_data.reset_index(inplace=True)

    return resampled_data

# Load and resample data 
data = pd.read_csv('DataFromApi.csv')

# Resample data to 15-minute intervals
resampled_data = resample_data(data, 15)

# Save resampled data to a new CSV file
resampled_data.to_csv('resampled_data.csv', index=False)

print("Processed and saved resampled_data.csv")
