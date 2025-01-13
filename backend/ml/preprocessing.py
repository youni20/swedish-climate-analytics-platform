import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.base import BaseEstimator, TransformerMixin
from typing import Tuple, List

class FeatureScaler(BaseEstimator, TransformerMixin):
    """
    Custom scaler for environmental data.
    """
    def __init__(self, method='standard'):
        self.method = method
        self.scaler = StandardScaler() if method == 'standard' else MinMaxScaler()
        self.feature_names = None

    def fit(self, X, y=None):
        self.feature_names = X.columns
        self.scaler.fit(X)
        return self

    def transform(self, X):
        return pd.DataFrame(self.scaler.transform(X), columns=self.feature_names, index=X.index)

class TimeSeriesSplitter:
    """
    Splits time-series data for training and testing.
    """
    def __init__(self, n_splits=5, test_size=0.2):
        self.n_splits = n_splits
        self.test_size = test_size

    def split(self, df: pd.DataFrame, date_col: str = 'timestamp') -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Simple temporal split.
        """
        df = df.sort_values(by=date_col)
        split_idx = int(len(df) * (1 - self.test_size))
        return df.iloc[:split_idx], df.iloc[split_idx:]
