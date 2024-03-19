import streaming_indicators as si

def getSuperTrend(candles):
  st_atr_length = 10
  st_factor = 3
  ST = si.SuperTrend(st_atr_length, st_factor)
  st_values = []
  for idx, candle in candles.iterrows():
        st = ST.update(candle)
        st_values.append(st) # Append the st value to the list
  return st_values 
