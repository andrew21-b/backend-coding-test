from fastapi import APIRouter
from app.controller.v1.endpoints import health, metric
api_router = APIRouter()

api_router.include_router(metric.router, prefix="/metrics", tags=["Metrics"])
api_router.include_router(health.router, tags=["Health"])