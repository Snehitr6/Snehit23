# Weather Monitoring System

This Weather Monitoring System is a Python-based application that continuously fetches weather data for specified cities and checks for any threshold alerts.

## Features

- Fetches real-time weather data for multiple cities
- Configurable city list and fetch interval
- Checks weather data against predefined thresholds
- Alerts for extreme weather conditions

## How It Works

1. The system reads a list of cities and a fetch interval from a configuration file.
2. It periodically fetches weather data for these cities using the `fetch_weather_for_cities` function.
3. The retrieved weather data is displayed in the console.
4. The system then checks the weather data against predefined thresholds using the `check_thresholds` function.
5. If any thresholds are exceeded, appropriate alerts are triggered.
6. This process repeats at the specified interval.

## Setup

1. Ensure you have Python installed on your system.
2. Install the required dependencies (list them in a `requirements.txt` file if applicable).
3. Set up your `config.py` file with the desired cities and fetch interval.
4. Implement the `weather_fetcher.py` and `alerts.py` modules according to your specific requirements.

## Usage

Run the script using:


The system will start monitoring and display weather data and any alerts in the console.

## Configuration

Edit the `config.py` file to modify:

- `CITIES`: List of cities to monitor
- `FETCH_INTERVAL`: Time interval (in seconds) between each weather data fetch

## Modules

- `main.py`: The main script that runs the monitoring loop
- `weather_fetcher.py`: Contains the `fetch_weather_for_cities` function to retrieve weather data
- `alerts.py`: Contains the `check_thresholds` function to check for and trigger alerts
- `config.py`: Contains configuration variables like `CITIES` and `FETCH_INTERVAL`

## Customization

You can extend this system by:

- Adding more sophisticated alert mechanisms
- Implementing a user interface for real-time monitoring
- Storing historical weather data for analysis
- Integrating with other systems or APIs for enhanced functionality

## Contributing

Contributions to improve the Weather Monitoring System are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

