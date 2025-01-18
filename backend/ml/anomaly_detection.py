import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from typing import Literal

class AnomalyDetector:
    def __init__(self, model_type: Literal['isolation_forest', 'dbscan'] = 'isolation_forest'):
        self.model_type = model_type
        self.model = None
        self.scaler = StandardScaler()

    def fit_predict(self, df: pd.DataFrame, features=['temperature', 'pressure', 'humidity']) -> pd.Series:
        X = df[features].dropna()
        X_scaled = self.scaler.fit_transform(X)

        if self.model_type == 'isolation_forest':
            self.model = IsolationForest(contamination=0.04, random_state=42)
            # Returns -1 for anomaly, 1 for normal
            preds = self.model.fit_predict(X_scaled)
        
        elif self.model_type == 'dbscan':
            self.model = DBSCAN(eps=0.5, min_samples=5)
            # Returns -1 for noise (anomaly)
            preds = self.model.fit_predict(X_scaled)
        
        # specific to scikit-learn anomaly detection: -1 is anomaly
        return pd.Series(preds, index=X.index).apply(lambda x: 1 if x == -1 else 0)
