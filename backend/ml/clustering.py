import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class CityClusterer:
    def __init__(self, n_clusters=4):
        self.n_clusters = n_clusters
        self.model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.scaler = StandardScaler()

    def fit_predict(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Expects a DataFrame where index is city and columns are aggregated features.
        """
        X_scaled = self.scaler.fit_transform(df)
        labels = self.model.fit_predict(X_scaled)
        
        result = df.copy()
        result['cluster'] = labels
        return result
