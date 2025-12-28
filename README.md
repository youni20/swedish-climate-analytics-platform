# Swedish Environmental Analytics & Forecasting Platform

A production-ready, full-stack machine learning platform that analyzes environmental data across Swedish cities, providing interactive visualizations, predictive analytics, and actionable insights.

![Dashboard Preview](https://via.placeholder.com/800x400?text=Dashboard+Preview)

## 🌟 Features

*   **Data Pipeline**: Robust ETL pipeline ingesting multi-source environmental data (CSV, Excel).
*   **Advanced Analytics**:
    *   **Forecasting**: Prophet & SARIMA models for accurate temperature and weather trends.
    *   **Anomaly Detection**: Isolation Forest & DBSCAN to identify environmental outliers.
    *   **Clustering**: K-Means analysis to group cities by climate patterns.
*   **Interactive Dashboard**:
    *   Real-time Leaflet map visualization.
    *   Dynamic charts using Recharts.
    *   City-specific detailed views.
    *   Dark/Light mode support.
*   **Modern Tech Stack**:
    *   **Backend**: FastAPI, Python 3.13, Pandas, Scikit-learn, Prophet.
    *   **Frontend**: React 18, TypeScript, Tailwind CSS, Vite.
    *   **Infrastructure**: Docker, Docker Compose, Redis caching, GitHub Actions CI/CD.

## 🚀 Getting Started

### Prerequisites

*   **Docker** and **Docker Compose**
*   **Node.js 18+** (for local frontend dev)
### 📊 Data Source

This project uses the **Sweden Cities Environmental Data** dataset.
*   **Source**: [Kaggle - Sweden Cities Environmental Data](https://www.kaggle.com/datasets/orvile/sweden-cities-environmental-data)
*   **License**: CC0: Public Domain

### 🐳 Quick Start (Docker)

The easiest way to run the full platform is with Docker Compose:

```bash
# Build and run all services
docker-compose up --build
```

Access the application:
*   **Frontend Dashboard**: [http://localhost](http://localhost)
*   **Backend API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

### 🛠️ Local Development

#### Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the API
uvicorn backend.api.main:app --reload
```

#### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## 🏗️ Architecture

The project follows a microservices-ready architecture:

1.  **Data Layer**: Raw CSV/Excel files processed into structured DataFrames.
2.  **ML Layer**: Scikit-learn and Prophet models for inference.
3.  **API Layer**: FastAPI handling requests, validation, and serving predictions.
4.  **Client Layer**: React SPA for visualization and user interaction.
5.  **Cache Layer**: Redis for storing frequent expensive query results.

## 🧪 Testing

Run the automated test suite:

```bash
# Run API validation tests
python backend/tests/test_api_script.py
```

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
