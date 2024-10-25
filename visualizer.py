import sqlite3
import matplotlib.pyplot as plt

def plot_daily_summary():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    
    c.execute('''SELECT date, avg_temp FROM daily_summary''')
    data = c.fetchall()
    
    if data:
        dates = [row[0] for row in data]
        avg_temps = [row[1] for row in data]
        
        plt.plot(dates, avg_temps, label='Average Temp (°C)')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Daily Average Temperature')
        plt.legend()
        plt.show()
    
    conn.close()





