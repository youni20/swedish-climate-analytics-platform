# Swedish Environmental Analytics & Forecasting Platform

A production-ready, full-stack machine learning platform that analyzes environmental data across Swedish cities, providing interactive visualizations, predictive analytics, and actionable insights.

## Features
- **Data Pipeline**: Robust ingestion of multi-source environmental data.
- **Forecasting**: Prophet & SARIMA models for temperature and weather trends.
- **Anomaly Detection**: Isolation Forest to spot environmental outliers.
- **Clustering**: K-Means analysis to group cities by climate similarity.
- **Interactive Dashboard**: React + TypeScript frontend with real-time visualizations.

## Tech Stack
- **Backend**: FastAPI, Python 3.13, Pandas, Scikit-learn, Prophet
- **Frontend**: React, TypeScript, Tailwind CSS, Recharts
- **Infrastructure**: Docker, Redis

## Setup
1. Clone the repository.
2. Install backend dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Run the data exploration notebook: `notebooks/01_data_exploration.ipynb`

## License
MIT
