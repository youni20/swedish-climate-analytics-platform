import pandas as pd
from typing import Dict, Optional
import logging
from backend.config import RAW_DATA_PATH, WEEKLY_DATA_PATH, DAILY_TRANSFORM_PATH, XLSX_DATA_PATH

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:
    """
    Handles loading of environmental datasets.
    """
    
    @staticmethod
    def load_raw_data(sample: bool = False, n_rows: int = 100000) -> pd.DataFrame:
        """
        Loads the main raw environmental dataset.
        Args:
            sample: If True, only loads n_rows.
            n_rows: Number of rows to load if sample is True.
        """
        path = RAW_DATA_PATH
        if not path.exists():
            raise FileNotFoundError(f"Dataset not found at {path}")
        
        logger.info(f"Loading raw data from {path}...")
        
        if sample:
            df = pd.read_csv(path, nrows=n_rows)
        else:
            # Optimize memory by specifying types if needed, for now let pandas infer
            df = pd.read_csv(path)
            
        logger.info(f"Loaded raw data with shape: {df.shape}")
        return df

    @staticmethod
    def load_weekly_data() -> pd.DataFrame:
        path = WEEKLY_DATA_PATH
        logger.info(f"Loading weekly data from {path}...")
        return pd.read_csv(path)

    @staticmethod
    def load_daily_transform_data() -> pd.DataFrame:
        path = DAILY_TRANSFORM_PATH
        logger.info(f"Loading daily transform data from {path}...")
        return pd.read_csv(path)

    @staticmethod
    def load_excel_data() -> pd.DataFrame:
        path = XLSX_DATA_PATH
        logger.info(f"Loading excel data from {path}...")
        return pd.read_excel(path)

    @staticmethod
    def load_all() -> Dict[str, pd.DataFrame]:
        return {
            "raw": DataLoader.load_raw_data(),
            "weekly": DataLoader.load_weekly_data(),
            "daily": DataLoader.load_daily_transform_data(),
             # Excel might be slow, load on demand or here
            "excel": DataLoader.load_excel_data()
        }
