from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.metric_service import get_metric_result
from app.schemas.metric_schema import MetricResult
from app.database.connection import get_session  # Adjust import if your session dependency is elsewhere

router = APIRouter()

@router.get("/{metric_id}", response_model=MetricResult)
def read_metric(metric_id: str, session: Session = Depends(get_session)):
    result = get_metric_result(metric_id=metric_id, session=session)
    if result is None:
        raise HTTPException(status_code=400, detail="Metric not found")
    return result