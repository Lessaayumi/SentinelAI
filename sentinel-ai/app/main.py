from fastapi import FastAPI
from app.api.routes_events import router as events_router
from app.api.routes_health import router as health_router

app = FastAPI(
    title="SentinelAI",
    version="0.1.0",
    description="Security Analytics and anomaly detection API."
)

app.include_router(health_router)
app.include_router(events_router, prefix="/api/v1")

@app.get("/")
def root():
    return {
        "name": "SentinelAI",
        "version": "0.1.0",
        "status": "running"
    }
