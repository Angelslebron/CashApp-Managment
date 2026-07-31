from datetime import datetime

from pydantic import BaseModel, Field


class MovementBase(BaseModel):
    description: str = Field(..., min_length=3, max_length=255)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=3, max_length=100)
    movement_type: str = Field(..., pattern="^(INCOME|EXPENSE)$")


class MovementCreate(MovementBase):
    pass

class MovementUpdate(BaseModel):
    description: str
    amount: float
    category: str
    movement_type: str

class MovementResponse(MovementBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }