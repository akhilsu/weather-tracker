import requests
import pandas as pd
from datetime import datetime

# OpenWeatherMap API Configuration
API_KEY = "6cf04c4d7c9f26da44ceea0adb3aa206"    #OpenWeatherMap API key
CITY = "Bangalore"                              #City
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Fetch weather data
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()

    # Extract relevant fields
    weather_data = {
        "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "City": [CITY],
        "Temperature (C)": [data["main"]["temp"]],
        "Humidity (%)": [data["main"]["humidity"]],
        "Weather Description": [data["weather"][0]["description"]]
    }

    # Save data to CSV
    df = pd.DataFrame(weather_data)
    file_name = "daily_weather.csv"

    # Append to CSV if it exists, otherwise create a new one
    try:
        existing_data = pd.read_csv(file_name)
        updated_data = pd.concat([existing_data, df])
        updated_data.to_csv(file_name, index=False)
    except FileNotFoundError:
        df.to_csv(file_name, index=False)

    print(f"Weather data for {CITY} saved to {file_name}.")
else:
    print("Failed to fetch weather data. Check your API key or city name.")