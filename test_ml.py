import sys
import os
import pandas as pd
import numpy as np
sys.path.append(os.getcwd())

from backend.ml.preprocessing import FeatureScaler, TimeSeriesSplitter
from backend.ml.forecasting import ProphetForecaster, SARIMAForecaster
from backend.ml.anomaly_detection import AnomalyDetector
from backend.ml.clustering import CityClusterer

def test_ml_pipeline():
    print("Generating synthetic data...")
    dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
    df = pd.DataFrame({
        'timestamp': dates,
        'temperature': np.sin(np.linspace(0, 10, 100)) * 10 + 15 + np.random.normal(0, 1, 100),
        'pressure': np.random.normal(1013, 5, 100),
        'humidity': np.random.normal(70, 10, 100),
        'city': 'TestCity'
    })
    
    print("Testing Feature Scaler...")
    scaler = FeatureScaler()
    scaled = scaler.fit_transform(df[['temperature', 'pressure']])
    print("Scalar output shape:", scaled.shape)
    
    print("Testing Prophet...")
    p_model = ProphetForecaster()
    p_model.fit(df)
    p_forecast = p_model.predict(periods=10)
    print("Prophet forecast shape:", p_forecast.shape)
    
    print("Testing SARIMA...")
    s_model = SARIMAForecaster()
    s_model.fit(df['temperature'])
    s_forecast = s_model.predict(steps=10)
    print("SARIMA forecast shape:", s_forecast.shape)
    
    print("Testing Anomaly Detection...")
    ad = AnomalyDetector(model_type='isolation_forest')
    anomalies = ad.fit_predict(df)
    print("Anomalies detected:", anomalies.sum())
    
    print("Testing Clustering...")
    # Create multi-city dummy data
    city_data = pd.DataFrame({
        'avg_temp': [10, 15, 5, 20],
        'avg_humidity': [80, 60, 90, 50]
    }, index=['CityA', 'CityB', 'CityC', 'CityD'])
    clusterer = CityClusterer(n_clusters=2)
    clustered = clusterer.fit_predict(city_data)
    print("Clusters assigned:", clustered['cluster'].unique())

if __name__ == "__main__":
    test_ml_pipeline()
