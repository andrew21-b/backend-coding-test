import uuid
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import Base

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    query_id = Column(String, ForeignKey("queries.id"), nullable=False)
    is_editable = Column(Boolean, default=True)

    query = relationship("Query", back_populates="metrics")

    layouts = relationship("Layout", back_populates="metric", cascade="all, delete-orphan")
