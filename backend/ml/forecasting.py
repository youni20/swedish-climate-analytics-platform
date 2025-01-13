import pandas as pd
import numpy as np
from prophet import Prophet
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import logging
from typing import Dict, Any, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProphetForecaster:
    def __init__(self):
        self.model = None

    def fit(self, df: pd.DataFrame, date_col='timestamp', target_col='temperature'):
        """
        Fits Prophet model. Requires columns 'ds' and 'y'.
        """
        df_prophet = df.rename(columns={date_col: 'ds', target_col: 'y'})
        self.model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
        self.model.fit(df_prophet)
        return self

    def predict(self, periods=30) -> pd.DataFrame:
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

class SARIMAForecaster:
    def __init__(self, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)):
        self.order = order
        self.seasonal_order = seasonal_order
        self.model = None
        self.results = None

    def fit(self, series: pd.Series):
        self.model = SARIMAX(series, order=self.order, seasonal_order=self.seasonal_order, enforce_stationarity=False, enforce_invertibility=False)
        self.results = self.model.fit(disp=False)
        return self

    def predict(self, steps=30) -> pd.Series:
        return self.results.forecast(steps=steps)

class ForecastEnsemble:
    """
    Combines predictions from multiple models.
    """
    def __init__(self):
        self.prophet = ProphetForecaster()
        self.sarima = SARIMAForecaster()

    def fit_predict(self, df: pd.DataFrame, target_col='temperature', periods=30):
        # Prophet
        self.prophet.fit(df, target_col=target_col)
        p_pred = self.prophet.predict(periods)
        
        # SARIMA (needs regular index)
        series = df.set_index('timestamp')[target_col].asfreq('D').fillna(method='ffill')
        self.sarima.fit(series)
        s_pred = self.sarima.predict(steps=periods)
        
        # Combine (align dates)
        ensemble = pd.DataFrame({
            'date': p_pred['ds'].iloc[-periods:].values,
            'prophet': p_pred['yhat'].iloc[-periods:].values,
            'sarima': s_pred.values,
            'ensemble': (p_pred['yhat'].iloc[-periods:].values + s_pred.values) / 2
        })
        return ensemble
