from fastapi import APIRouter
from typing import Dict, List
import pandas as pd
from backend.data.loader import DataLoader
from backend.ml.clustering import CityClusterer
from backend.data.processor import DataProcessor

router = APIRouter()

# MVP Cache
loader = DataLoader()
try:
    df_raw = loader.load_raw_data(sample=True, n_rows=50000)
    df = DataProcessor.clean_raw_data(df_raw)
except:
    df = pd.DataFrame()

@router.get("/clusters")
def get_city_clusters():
    if df.empty:
        return {"clusters": []}
        
    try:
        # Prepare data for clustering (pivot by city and month/feature)
        # Simplified: mean temperature and humidity by city
        city_stats = df.groupby('city')[['temperature', 'humidity']].mean().reset_index()
        
        clusterer = CityClusterer(n_clusters=3)
        # CityClusterer expects features, let's adapt or use it simply
        # The existing CityClusterer.cluster method takes a dataframe and returns it with 'cluster' col
        
        # We need to reshape slightly for the specific implementation or just use scikit directly here for MVP speed
        # Let's check existing implementation usage in test_ml.py or class
        # Assuming fit_predict style
        
        # Quick inline clustering for endpoint
        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters=3, random_state=42)
        city_stats['cluster'] = kmeans.fit_predict(city_stats[['temperature', 'humidity']].fillna(0))
        
        return city_stats.to_dict(orient='records')
    except Exception as e:
        return {"error": str(e), "clusters": []}

@router.get("/correlations")
def get_correlations():
    if df.empty:
        return {}
    
    # Calculate correlation matrix
    corr = df[['temperature', 'humidity', 'pressure', 'wind_speed']].corr()
    # Format for heatmap (x, y, value)
    data = []
    for col1 in corr.columns:
        for col2 in corr.columns:
            data.append({
                "x": col1,
                "y": col2,
                "value": round(corr.loc[col1, col2], 2)
            })
    return data
