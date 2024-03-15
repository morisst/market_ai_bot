import pandas as pd

# Function to resample data
def resample_data(data, interval):
    # Convert interval to milliseconds
    interval_millis = interval * 60 * 1000

    # Convert the 'time' column to datetime
    data['time'] = pd.to_datetime(data['time'], unit='ms')

    # Set the 'time' column as the index
    data.set_index('time', inplace=True)

    # Resample the data to the specified interval
    resampled_data = data.resample(f'{interval}T').agg({
        'open': 'first',
        'close': 'last',
        'high': 'max',
        'low': 'min',
        'volume': 'sum',
        'ShouldBuy': 'first',
        'MovingAverage20': lambda x: x.iloc[-20:].mean(),
        'MovingAverage50': lambda x: x.iloc[-50:].mean(),
        'MovingAverage100': lambda x: x.iloc[-100:].mean()
    })

    resampled_data.dropna(inplace=True)

    # Reset the index
    resampled_data.reset_index(inplace=True)

    # Convert the 'time' column back to milliseconds
    resampled_data['time'] = resampled_data['time'].astype(int) // (1000 * 1000)

    return resampled_data

# Load and resample data from CSV
data = pd.read_csv('data_to_train/NIFTY 50.csv')

# Resample data to 15-minute intervals
resampled_data = resample_data(data, 15)

# Save resampled data to a new CSV file
resampled_data.to_csv('resampled_data.csv', index=False)

print("Processed and saved resampled_data.csv")
