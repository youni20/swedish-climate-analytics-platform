# Deployment Guide

## Production Deployment

### Requirements
- A Linux server (Ubuntu 22.04 LTS recommended).
- Docker and Docker Compose installed.

### Steps

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/swedish-climate-platform.git
    cd swedish-climate-platform
    ```

2.  **Environment Setup**
    - Copy `.env.example` to `.env` and configure secrets.
    ```bash
    cp .env.example .env
    ```

3.  **Build and Run**
    ```bash
    docker-compose -f docker-compose.yml up -d --build
    ```

4.  **Verification**
    - Check logs: `docker-compose logs -f`
    - Verify health endpoint: `curl http://localhost:8000/health`

## Scaling
- Factors to consider:
    - **Redis**: Externalize Redis (e.g., AWS ElastiCache) for persistence.
    - **Load Balancing**: Use Nginx or ALB for traffic distribution.
    - **ML Workers**: Offload heavy training jobs to Celery workers.
