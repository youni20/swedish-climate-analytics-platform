import os
from pathlib import Path

# Project Dirs
BACKEND_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BACKEND_DIR.parent
DATASETS_DIR = PROJECT_DIR / "datasets"

PROJECT_NAME = "Swedish Environmental Analytics Platform"
API_V1_STR = "/api/v1"



# Dataset Paths
RAW_DATA_PATH = DATASETS_DIR / "swedish_cities_environmental.csv"
WEEKLY_DATA_PATH = DATASETS_DIR / "swedish cities environmental_week.csv"
DAILY_TRANSFORM_PATH = DATASETS_DIR / "swedish cities environmental_tranformDay.csv"
XLSX_DATA_PATH = DATASETS_DIR / "Sweden_Cities_Avg_DaySect.xlsx"

# Processing Config
RANDOM_SEED = 42
TEST_SPLIT_SIZE = 0.2
