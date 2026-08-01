from pydantic import BaseModel


class PredictionRequest(BaseModel):

    description: str


class PredictionResponse(BaseModel):

    category: str