from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from api.database import Base


class Movement(Base):
    __tablename__ = "movements"

    id = Column(Integer, primary_key=True, index=True)

    description = Column(String(255), nullable=False)

    amount = Column(Float, nullable=False)

    category = Column(String(100), nullable=False)

    movement_type = Column(String(20), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)