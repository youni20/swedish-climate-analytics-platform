from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import API_V1_STR, PROJECT_NAME
from backend.api.routes import cities, predictions, analytics

app = FastAPI(
    title=PROJECT_NAME,
    openapi_url=f"{API_V1_STR}/openapi.json"
)

# CORS
origins = [
    "http://localhost",
    "http://localhost:3000", # React default
    "http://localhost:5173", # Vite default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(cities.router, prefix="/api/cities", tags=["cities"])
app.include_router(predictions.router, prefix="/api/predictions", tags=["predictions"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])

@app.get("/health")
def health_check():
    """
    Health check endpoint to verify backend status.
    """
    return {"status": "healthy"}
