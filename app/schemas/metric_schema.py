from pydantic import BaseModel
from typing import Optional

class MetricResult(BaseModel):
    day: Optional[str] = None
    cost_avoided: Optional[float] = None
    total_alerts: Optional[int] = None
    alert_type: Optional[str] = None
    total_flagged: Optional[int] = None
    avg_per_day: Optional[float] = None
    amount: Optional[float] = None
    need_approval_count: Optional[int] = None

    class Config:
        from_attributes = True