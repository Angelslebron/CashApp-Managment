from sqlalchemy import Column, Integer, String, Float, Date
from api.database import Base


class Movement(Base):

    __tablename__ = "movements"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    description = Column(
        String,
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    category = Column(
        String,
        nullable=False
    )

    date = Column(
        Date,
        nullable=False
    )