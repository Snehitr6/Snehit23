import sqlite3

def create_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                city TEXT,
                temp REAL,
                feels_like REAL,
                condition TEXT,
                timestamp INTEGER
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS daily_summary (
                city TEXT,
                avg_temp REAL,
                max_temp REAL,
                min_temp REAL,
                dominant_condition TEXT,
                date TEXT
                )''')
    conn.commit()
    conn.close()

def store_weather_data(city, temp, feels_like, condition, timestamp):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("INSERT INTO weather_data VALUES (?, ?, ?, ?, ?)",
              (city, temp, feels_like, condition, timestamp))
    conn.commit()
    conn.close()
