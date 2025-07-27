import structlog
from fastapi import FastAPI
from app.context.config import settings
from app.controller.v1.routes import api_router






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
app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": settings.PROJECT_NAME, "status": "running"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)