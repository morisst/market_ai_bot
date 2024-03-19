from json import load
from Indicators.SuperTrend import getSuperTrend
import pandas as pd
df = pd.read_csv('DataFromApi.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.sort_values(by='Timestamp')

candles = df[['open', 'high', 'low', 'close',]]

st_values = getSuperTrend(candles)

df['ST'] = st_values

new_csv_file_path = 'DataFromApiWithST.csv'
df.to_csv(new_csv_file_path, index=False)

print(f"New CSV file created: {new_csv_file_path}")