import requests
from datetime import datetime, timezone
from config import API_KEY, CITIES

# Function to convert temperature from Kelvin to Celsius
def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

# Function to fetch weather data for a specific city
def fetch_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': city,
            'condition': data['weather'][0]['main'],
            'temp': kelvin_to_celsius(data['main']['temp']),
            'feels_like': kelvin_to_celsius(data['main']['feels_like']),
            # Using timezone-aware datetime conversion
            'timestamp': datetime.fromtimestamp(data['dt'], tz=timezone.utc)
        }
        return weather
    else:
        print(f"Failed to fetch data for {city}. Status code: {response.status_code}")
        return None

# Function to fetch weather data for multiple cities
def fetch_weather_for_cities(cities):
    weather_data = []
    for city in cities:
        weather = fetch_weather(city)
        if weather:
            weather_data.append(weather)
    return weather_data

if __name__ == "__main__":
    # Fetch weather data for cities specified in the config
    weather_data = fetch_weather_for_cities(CITIES)
    print(weather_data)
