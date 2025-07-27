from sqlalchemy import Column, String, Text
from sqlalchemy.orm import DeclarativeBase,relationship

class Base(DeclarativeBase):
    pass

class Query(Base):
    __tablename__ = "queries"

    id = Column(String, primary_key=True)
    query = Column(Text, nullable=False)


    metrics = relationship("Metric", back_populates="query", cascade="all, delete-orphan")