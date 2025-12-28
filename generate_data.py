import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data():
    cities = ['Stockholm', 'Gothenburg', 'Malmö', 'Uppsala', 'Västerås']
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 12, 31)
    
    data = []
    
    # Generate daily data for each city
    for city in cities:
        current_date = start_date
        while current_date <= end_date:
            # Base temp varies by month
            month = current_date.month
            base_temp = 5 + 15 * np.sin((month - 4) * np.pi / 6)
            
            # Daily variation
            temp = base_temp + np.random.normal(0, 3)
            humidity = np.clip(60 + np.random.normal(0, 10), 30, 100)
            pressure = 1013 + np.random.normal(0, 5)
            wind_speed = np.abs(np.random.normal(5, 2))
            
            data.append({
                'city': city,
                'timestamp': current_date.isoformat(),
                'temperature': round(temp, 1),
                'humidity': round(humidity, 1),
                'pressure': round(pressure, 1),
                'wind_speed': round(wind_speed, 1),
                'id': f"{city}_{current_date.strftime('%Y%m%d')}"
            })
            current_date += timedelta(days=1)
            
    df = pd.DataFrame(data)
    df.to_csv('datasets/swedish_cities_environmental.csv', index=False)
    print(f"Generated {len(df)} rows of data.")

if __name__ == "__main__":
    generate_data()
