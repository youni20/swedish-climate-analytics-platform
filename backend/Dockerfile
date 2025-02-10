# Use an official Python runtime as a parent image
# Python 3.13 is relatively new, 3.12 is safer for general ML compatibility currently, 
# but user specifically verified 3.13 compat earlier.
FROM python:3.13-slim

# Set work directory
WORKDIR /app

# Install system dependencies
# gcc and python3-dev might be needed for some numpy/pandas extensions if wheels aren't found
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY backend/ ./backend/
# Also need to copy datasets if they are needed for the MVP loader
# In a real prod environment, data might be mounted or pulled from S3
COPY datasets/ ./datasets/

# Expose port
EXPOSE 8000

# Set environment variables
ENV PYTHONPATH=/app
ENV APP_ENV=production

# Run app
CMD ["uvicorn", "backend.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
