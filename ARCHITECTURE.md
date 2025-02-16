# System Architecture

## Overview
The Swedish Environmental Analytics Platform is designed as a modular, containerized application.

## Components

### 1. Backend (FastAPI)
- **Role**: Serves API endpoints, runs ML models, handles data processing.
- **Key Libraries**: `fastapi`, `pandas`, `scikit-learn`, `prophet`.
- **Structure**:
    - `api/`: Routes and schemas.
    - `data/`: Data loading and cleaning logic.
    - `ml/`: Model definitions (Forecasting, Anomaly Detection).

### 2. Frontend (React)
- **Role**: User interface for visualization.
- **Key Libraries**: `react`, `typescript`, `tailwindcss`, `recharts`, `leaflet`.
- **State Management**: React Query (TanStack Query).

### 3. Data Storage
- **Primary**: Local filesystem (CSV/Excel) for the MVP.
- **Caching**: Redis for API response caching.

### 4. DevOps
- **Docker**: Containerization of services.
- **Docker Compose**: Orchestration.
- **GitHub Actions**: CI pipeline for testing.
