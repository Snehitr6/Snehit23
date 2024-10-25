TEMP_THRESHOLD = 30  # Example threshold

def check_thresholds(weather_data):
    print(f"Checking {len(weather_data)} weather entries")  # Debugging
    for data in weather_data:
        if data['temp'] > TEMP_THRESHOLD:
            print(f"Alert! Temperature in {data['city']} exceeded {TEMP_THRESHOLD}°C.")

def check_for_alerts(weather_data):
    check_thresholds(weather_data)
