from json import load
from Indicators.SuperTrend import getSuperTrend
import pandas as pd

df = pd.read_csv('DataFromApiWithST.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.sort_values(by='Timestamp')

for index, row in df.iterrows():
  timestamp = row['Timestamp']
  open_price = row['open']
  high_price = row['high']
  low_price = row['low']
  close_price = row['close']
  volume = row['volume']
  st = row['ST'] # Assuming 'ST' is the column name for the SuperTrend values

  # You can now use these values as needed
  print(f"Timestamp: {timestamp}, Close: {close_price}, Volume: {volume}, ST: {st}")