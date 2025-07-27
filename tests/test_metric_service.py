import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from app.models.metric import Metric
from app.models.query import Query
from app.schemas.metric_schema import MetricResult
from app.services.metric_service import get_metric_result

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    yield session
    session.close()

def setup_test_data(session):
    query = Query(id="test_query_id", query="SELECT 1 AS cost_avoided")
    metric = Metric(id="test_metric_id", query_id="test_query_id", is_editable=True)
    session.add(query)
    session.add(metric)
    session.commit()

def test_get_metric_result_found(session):
    setup_test_data(session)
    result = get_metric_result(session, "test_metric_id")
    print(f"Result found: {result}")
    assert isinstance(result, list)
    assert isinstance(result[0], MetricResult)
    assert result[0].cost_avoided == 1

def test_get_metric_result_metric_not_found(session):
    result = get_metric_result(session, "missing_id")
    assert result is None

def test_get_metric_result_query_not_found(session):
    metric = Metric(id="no_query_metric", query_id="missing_query", is_editable=True)
    session.add(metric)
    session.commit()
    result = get_metric_result(session, "no_query_metric")
    assert result is None

def test_get_metric_result_empty_query_result(session):
    query = Query(id="empty_query_id", query="SELECT cost_avoided FROM (SELECT 1 AS cost_avoided) WHERE 0")
    metric = Metric(id="empty_metric_id", query_id="empty_query_id", is_editable=True)
    session.add(query)
    session.add(metric)
    session.commit()
    result = get_metric_result(session, "empty_metric_id")
    assert result == []


def test_get_metric_result_multiple_rows(session):
    query = Query(id="multi_query_id", query="SELECT 1 AS cost_avoided UNION SELECT 2 AS cost_avoided")
    metric = Metric(id="multi_metric_id", query_id="multi_query_id", is_editable=True)
    session.add(query)
    session.add(metric)
    session.commit()
    result = get_metric_result(session, "multi_metric_id")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0].cost_avoided == 1
    assert result[1].cost_avoided == 2