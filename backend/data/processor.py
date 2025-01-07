import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    """
    Handles preprocessing and cleaning of environmental data.
    """
    
    @staticmethod
    def clean_raw_data(df: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans the raw dataset.
        - Converts timestamp to datetime
        - Handles duplicates
        - Sorts by time
        """
        logger.info("Cleaning raw data...")
        df = df.copy()
        
        # Convert timestamp
        # The sample showed: 2022-09-26 07:43:37.333989+00:00
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Drop duplicates if id exists
        if 'id' in df.columns:
            df = df.drop_duplicates(subset=['id'])
        
        # Sort
        if 'city' in df.columns and 'timestamp' in df.columns:
            df = df.sort_values(by=['city', 'timestamp'])
            
        return df

    @staticmethod
    def get_city_stats(df: pd.DataFrame) -> pd.DataFrame:
        """
        Returns basic stats per city.
        """
        return df.groupby('city')['temperature'].describe()
