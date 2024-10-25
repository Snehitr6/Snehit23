# main.py

import time
from alerts import check_thresholds
from weather_fetcher import fetch_weather_for_cities  # Import the new function
from config import CITIES, FETCH_INTERVAL  # Import CITIES and FETCH_INTERVAL from config.py

def run_monitoring():
    while True:
        # Fetch weather data for cities specified in the config
        weather_data = fetch_weather_for_cities(CITIES)
        
        # Check if we received any data
        if weather_data:
            print("Weather data retrieved:")
            for weather in weather_data:
                print(weather)  # Print each city's weather data

            # Check for alerts with the collected weather data
            check_thresholds(weather_data)
        else:
            print("No weather data retrieved.")

        # Wait for the specified fetch interval before fetching data again
        time.sleep(FETCH_INTERVAL)

if __name__ == "__main__":
    run_monitoring()
