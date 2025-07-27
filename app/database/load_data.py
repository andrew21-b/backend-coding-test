import json
import pandas as pd
from app.database.connection import get_session
from app.models.query import Query
from app.models.metric import Metric


def load_csv_to_database():
    df_queries = pd.read_csv("data/queries.csv")
    session = next(get_session())

    for _, row in df_queries.iterrows():
        query_obj = Query(id=row["id"], query=row["query"])
        session.merge(query_obj)
    session.commit()
    session.close()


def load_json_to_database():
    with open("data/metrics.json", "r") as f:
        data = json.load(f)

    session = next(get_session())
    for item in data["items"]:
        metric_obj = Metric(
            id=item["id"],
            query_id=item.get("queryId") or item.get("query_id"),
            is_editable=item.get("isEditable", True),
        )
        session.merge(metric_obj)


    session.commit()
    session.close()


load_csv_to_database()
load_json_to_database()
