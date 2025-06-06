import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        print("API Key not found. Check your .env file.")
        return

    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(URL)
        data = response.json()

        if response.status_code == 200:

            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            print(f"Weather in {city.capitalize()}:")
            print(f"Temperature: {temperature}°C")
            print(f"Condition: {description}")
            print(f"Humidity: {humidity}%")
        else:
            print(f"Error: {data.get('message', 'Unknown error')}")

    except requests.exceptions.RequestException as e:
        print("Network error:", e)

city = input("Enter city name: ")
get_weather(city)
