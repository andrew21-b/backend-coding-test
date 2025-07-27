from sqlalchemy.orm import Session
from sqlalchemy import text
from app.models.metric import Metric
from app.models.query import Query
from app.schemas.metric_schema import MetricResult

def get_metric_result(session: Session, metric_id: str):
    metric = check_metric_exists(session, metric_id)
    if not metric:
        return None

    query_obj = get_query_by_metric_id(session, metric)
    if not query_obj:
        return None

    result = session.execute(text(query_obj.query))
    rows = result.fetchall()
    columns = result.keys() if rows else []
    data = [MetricResult(**dict(zip(columns, row))) for row in rows]

    return data

def check_metric_exists(session: Session, metric_id: str):
    return session.query(Metric).filter(Metric.id == metric_id).first()

def get_query_by_metric_id(session: Session, metric: Metric):
    return session.query(Query).filter(Query.id == metric.query_id).first()