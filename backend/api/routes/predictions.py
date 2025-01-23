from fastapi import APIRouter, HTTPException
from backend.api.schemas.schemas import ForecastResponse, AnomalyResponse, ForecastPoint, AnomalyPoint
from backend.ml.forecasting import ProphetForecaster
from backend.ml.anomaly_detection import AnomalyDetector
from backend.data.loader import DataLoader
from backend.data.processor import DataProcessor
import pandas as pd

router = APIRouter()

# Basic cache/state for MVP
loader = DataLoader()
try:
    df_raw = loader.load_raw_data(sample=True, n_rows=50000)
    df = DataProcessor.clean_raw_data(df_raw)
except:
    df = pd.DataFrame()

@router.get("/{city}/forecast", response_model=ForecastResponse)
def get_forecast(city: str, days: int = 30):
    """
    Generate future forecasts for a specific city using trained models.
    """
    if df.empty:
         raise HTTPException(status_code=503, detail="Data unavailable")
         
    city_data = df[df['city'] == city]
    if city_data.empty:
        raise HTTPException(status_code=404, detail="City not found")
        
    # Fit model on the fly (MVP - in production use pre-trained models)
    model = ProphetForecaster()
    try:
        model.fit(city_data)
        preds = model.predict(periods=days)
    except Exception as e:
         raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
    
    # Format response
    forecast_points = []
    # Take only the future part
    future_preds = preds.tail(days)
    for _, row in future_preds.iterrows():
        forecast_points.append(ForecastPoint(
            date=row['ds'],
            predicted_value=row['yhat'],
            lower_bound=row['yhat_lower'],
            upper_bound=row['yhat_upper']
        ))
        
    return ForecastResponse(city=city, model="Prophet", forecast=forecast_points)

@router.get("/{city}/anomalies", response_model=AnomalyResponse)
def get_anomalies(city: str):
    if df.empty:
        raise HTTPException(status_code=503, detail="Data unavailable")
        
    city_data = df[df['city'] == city]
    if city_data.empty:
        raise HTTPException(status_code=404, detail="City not found")
        
    detector = AnomalyDetector()
    try:
        # Use available numeric features
        numeric_df = city_data.select_dtypes(include=['float64', 'int64'])
        # Drop id if present
        if 'id' in numeric_df.columns:
            numeric_df = numeric_df.drop('id', axis=1)
            
        anomalies_mask = detector.fit_predict(numeric_df)
        
        # Combine with dates
        results = []
        # anomalies_mask is a Series 0/1. 1 is anomaly in our previous code logic? 
        # Checking previous code: "return pd.Series(preds, index=X.index).apply(lambda x: 1 if x == -1 else 0)"
        # Wait, if IsolationForest returns -1 for anomaly, lambda x: 1 if x == -1 else 0 means 1 IS ANOMALY. Correct.
        
        # We need to map back to original indices to get dates
        # The detector drops NAs, so we align indices
        aligned_df = city_data.loc[anomalies_mask.index]
        
        for idx, is_anom in anomalies_mask.items():
            if is_anom == 1:
                row = aligned_df.loc[idx]
                results.append(AnomalyPoint(
                    date=row['timestamp'],
                    is_anomaly=True,
                    value=row['temperature'] # reporting temp as primary metric
                ))
                
    except Exception as e:
        # Fallback empty
        print(e)
        results = []
        
    return AnomalyResponse(city=city, anomalies=results)
