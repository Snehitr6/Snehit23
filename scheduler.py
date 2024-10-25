import schedule
import time
from daily_summary import collect_weather_data, calculate_daily_summary, reset_daily_data

# Schedule data collection every 5 minutes
def run_weather_collection():
    collect_weather_data()
    print("Weather data collected.")

# Schedule daily summary calculation at the end of the day (e.g., 11:59 PM)
def run_daily_summary():
    # No need for 'global' if you're not modifying the variable
    summary = calculate_daily_summary()
    if summary:
        print("Daily Weather Summary:", summary)
    
    # Reset data after summary calculation
    reset_daily_data()

# Scheduling tasks
schedule.every(5).minutes.do(run_weather_collection)
schedule.every().day.at("23:59").do(run_daily_summary)

if __name__ == "__main__":
    print("Scheduler is running...")
    while True:
        schedule.run_pending()
        time.sleep(1)
