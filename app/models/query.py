from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from app.models.base import Base

class Query(Base):
    __tablename__ = "queries"

    id = Column(String, primary_key=True)
    query = Column(Text, nullable=False)


    metrics = relationship("Metric", back_populates="query", cascade="all, delete-orphan")