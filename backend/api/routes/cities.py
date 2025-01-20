from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from backend.api.schemas.schemas import City, WeatherData
from backend.data.loader import DataLoader
from backend.data.processor import DataProcessor
import pandas as pd

router = APIRouter()

# Instantiate loader once (in production use dependency injection with lru_cache)
loader = DataLoader()
# Load data into memory for MVP speed
try:
    df_raw = loader.load_raw_data(sample=True, n_rows=100000) 
    df = DataProcessor.clean_raw_data(df_raw)
except Exception:
    df = pd.DataFrame() # Fallback

@router.get("/", response_model=List[City])
def get_cities():
    if df.empty:
        return []
    cities = df['city'].unique()
    return [{"name": city} for city in cities]

@router.get("/{city}/current", response_model=WeatherData)
def get_city_current(city: str):
    if df.empty:
        raise HTTPException(status_code=503, detail="Data not available")
    
    city_data = df[df['city'] == city]
    if city_data.empty:
        raise HTTPException(status_code=404, detail="City not found")
        
    latest = city_data.iloc[-1]
    return WeatherData(
        timestamp=latest['timestamp'],
        temperature=latest['temperature'],
        pressure=latest.get('pressure'),
        humidity=latest.get('humidity'),
        wind_speed=latest.get('wind_speed'),
        city=city
    )

@router.get("/{city}/history", response_model=List[WeatherData])
def get_city_history(city: str, limit: int = 100):
    if df.empty:
        return []
        
    city_data = df[df['city'] == city]
    if city_data.empty:
        raise HTTPException(status_code=404, detail="City not found")
    
    # Return last 'limit' records
    records = city_data.tail(limit).to_dict(orient='records')
    return records
