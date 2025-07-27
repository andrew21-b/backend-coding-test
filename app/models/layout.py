from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.query import Base

class Layout(Base):
    __tablename__ = "layouts"

    id = Column(UUID(as_uuid=True), ForeignKey("metrics.id"), primary_key=True)
    screen_size = Column(String, primary_key=True)
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)
    w = Column(Integer, nullable=False)
    h = Column(Integer, nullable=False)
    static = Column(Boolean, nullable=True)


    metric = relationship("Metric", back_populates="layouts")
