import sqlite3
from collections import Counter
import datetime

def calculate_daily_summary():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    
    today = datetime.datetime.now().date()
    start_timestamp = int(datetime.datetime.combine(today, datetime.time.min).timestamp())
    end_timestamp = int(datetime.datetime.combine(today, datetime.time.max).timestamp())
    
    c.execute('''SELECT city, temp, condition FROM weather_data
                 WHERE timestamp BETWEEN ? AND ?''', (start_timestamp, end_timestamp))
    data = c.fetchall()
    
    if data:
        avg_temp = sum([row[1] for row in data]) / len(data)
        max_temp = max([row[1] for row in data])
        min_temp = min([row[1] for row in data])
        conditions = [row[2] for row in data]
        dominant_condition = Counter(conditions).most_common(1)[0][0]
        
        c.execute('''INSERT INTO daily_summary (city, avg_temp, max_temp, min_temp, dominant_condition, date)
                     VALUES (?, ?, ?, ?, ?, ?)''', (data[0][0], avg_temp, max_temp, min_temp, dominant_condition, today))
        conn.commit()
    
    conn.close()
