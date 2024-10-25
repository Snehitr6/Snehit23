from datetime import datetime
from weather_fetcher import fetch_weather_for_cities
from config import CITIES

# Storage for daily weather data
daily_weather_data = []

# Function to collect weather data and add to daily storage
def collect_weather_data():
    global daily_weather_data
    weather_data = fetch_weather_for_cities(CITIES)
    if weather_data:
        daily_weather_data.extend(weather_data)

# Function to calculate daily summary from collected data
def calculate_daily_summary():
    if not daily_weather_data:
        print("No data collected yet.")
        return None
    
    temp_values = [data['temp'] for data in daily_weather_data]
    conditions = [data['condition'] for data in daily_weather_data]

    daily_summary = {
        'average_temp': sum(temp_values) / len(temp_values),
        'max_temp': max(temp_values),
        'min_temp': min(temp_values),
        'dominant_condition': max(set(conditions), key=conditions.count),
        'date': datetime.now().strftime("%Y-%m-%d")
    }

    return daily_summary

# Function to reset data at the end of the day
def reset_daily_data():
    global daily_weather_data
    daily_weather_data = []

# To simulate a run for daily summary calculation
if __name__ == "__main__":
    # Simulate data collection (replace with actual periodic calls)
    collect_weather_data()

    # Simulate daily summary calculation
    summary = calculate_daily_summary()
    if summary:
        print("Daily Weather Summary:", summary)
    
    # Reset data after calculating summary
    reset_daily_data()
