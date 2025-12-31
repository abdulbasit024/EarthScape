import os
import csv
import json
import random
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.getcwd(), 'hdfs_mock', 'raw_data')
os.makedirs(DATA_DIR, exist_ok=True)

def generate_weather_data(num_records=100):
    stations = ['WS-001', 'WS-002', 'WS-003', 'WS-004', 'WS-005']
    start_date = datetime.now() - timedelta(days=30)
    
    filename = os.path.join(DATA_DIR, 'weather_stations.csv')
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['StationID', 'Date', 'Temperature', 'Humidity', 'Precipitation'])
        
        for i in range(num_records):
            station = random.choice(stations)
            date = (start_date + timedelta(days=i % 30)).strftime('%Y-%m-%d')
            temp = round(random.uniform(15.0, 35.0), 2)
            humidity = round(random.uniform(30.0, 90.0), 2)
            precip = round(random.uniform(0.0, 50.0), 2)
            
            writer.writerow([station, date, temp, humidity, precip])
    
    print(f"Generated {filename}")

def generate_satellite_metadata(num_records=50):
    satellites = ['SAT-A', 'SAT-B', 'SAT-C']
    start_date = datetime.now() - timedelta(days=30)
    
    filename = os.path.join(DATA_DIR, 'satellite_data.json')
    data = []
    
    for i in range(num_records):
        record = {
            'SatelliteID': random.choice(satellites),
            'Timestamp': (start_date + timedelta(hours=i)).isoformat(),
            'CloudCover': round(random.uniform(0.0, 100.0), 2),
            'Region': random.choice(['North', 'South', 'East', 'West'])
        }
        data.append(record)
        
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"Generated {filename}")

if __name__ == '__main__':
    generate_weather_data()
    generate_satellite_metadata()
