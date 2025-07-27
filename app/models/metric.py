from sqlalchemy import Column, PrimaryKeyConstraint, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class Metric(Base):
    __tablename__ = "metrics"

    id = Column(String, nullable=False)
    query_id = Column(String, ForeignKey("queries.id"), nullable=False)
    is_editable = Column(Boolean, default=True)

    __table_args__ = (PrimaryKeyConstraint("id", "query_id"),)

    query = relationship("Query", back_populates="metrics")

