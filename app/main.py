import structlog
from datetime import datetime, date
from decimal import Decimal
from typing import Optional
from sqlmodel import SQLModel, Field,Boolean,  create_engine, Session, select, Column
from sqlalchemy import Index, text, String, DateTime, Numeric
from fastapi import APIRouter, FastAPI
from app.context.config import Settings
from app.controller.v1.endpoints import health






# Configure logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="ISO"),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),

    cache_logger_on_first_use=True,
)

log = structlog.get_logger()


# FastAPI app
app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.VERSION)

api_router = APIRouter(prefix="/v1")

api_router.include_router(health.router, tags=["Health"])

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": Settings.PROJECT_NAME, "status": "running"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)