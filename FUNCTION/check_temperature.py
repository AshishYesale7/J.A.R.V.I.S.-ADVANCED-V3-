import requests
import json
from NetHyTech_Pyttsx3_Speak import *



def get_temperature_openweathermap(city):
    api_key = "57750a40690b5a50f53cc755c386cfbc"  # Replace with your actual OpenWeatherMap API key
    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    # send GET request to API endpoint
    response = requests.get(endpoint, params={"q": city, "appid": api_key, "units": "metric"})

    # check if the request was successful
    if response.status_code == 200:
        # parse JSON response
        data = json.loads(response.text)

        # check if 'main' key is present
        if 'main' in data:
            # extract temperature in Celsius
            temperature_celsius = data["main"]["temp"]
            return temperature_celsius
        else:
            print("Error: 'main' key not found in API response")
    else:
        print(f"Error: Failed to fetch data from API. Status code: {response.status_code}")

    return None


def Temp():
    city = "Harohalli, Karnataka"

    # get temperature using OpenWeatherMap API
    temperature_celsius = get_temperature_openweathermap(city)

    if temperature_celsius is not None:
        speak(f"The weather in {city} is {temperature_celsius}°C",2)
    else:
        print("Temperature data not available.")


