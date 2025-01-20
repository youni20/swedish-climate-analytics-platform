from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime

class City(BaseModel):
    name: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class WeatherData(BaseModel):
    timestamp: datetime
    temperature: float
    pressure: Optional[float] = None
    humidity: Optional[float] = None
    wind_speed: Optional[float] = None
    city: str

class ForecastPoint(BaseModel):
    date: datetime
    predicted_value: float
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None

class ForecastResponse(BaseModel):
    city: str
    model: str
    forecast: List[ForecastPoint]

class AnomalyPoint(BaseModel):
    date: datetime
    # 1 for anomaly, 0 for normal in our simplified model, but could be score
    is_anomaly: bool 
    value: float

class AnomalyResponse(BaseModel):
    city: str
    anomalies: List[AnomalyPoint]
