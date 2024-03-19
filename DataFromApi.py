import requests
import datetime
from json import dump,load
import os
import csv
import json

interval = ['1minute','30minute','day','week','month']
intrument_key = "NSE_EQ|INE742F01042"
date2 =datetime.date(2023, 8, 1)
date1 =datetime.date(2024, 3, 20)
url = "https://api.upstox.com/v2/historical-candle/"+intrument_key+"/"+interval[1]+"/"+str(date1)+"/"+str(date2)
intraday_url = "https://api.upstox.com/v2/historical-candle/intraday/"+intrument_key+"/"+interval[0]

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)
with open('DataFromApi.json', 'w') as file:
  dump(response.json(), file)



# Step 1: Read the JSON data
with open('DataFromApi.json', 'r') as file:
    data = json.load(file)

# Extract the candles data
candles = data['data']['candles']

# Define the CSV file name
csv_file_name = 'DataFromApi.csv'

# Define the header row for the CSV file
header = ['Timestamp', 'open', 'high', 'low', 'close', 'Volume', 'Other']

# Open the CSV file and write the header
with open(csv_file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    
    # Write the data rows
    for candle in candles:
        writer.writerow(candle)

print(f"CSV file '{csv_file_name}' has been created.")
