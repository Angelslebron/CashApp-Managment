from fastapi import APIRouter

from api.ai.classifier import predict_category
from api.schemas.prediction import (
    PredictionRequest,
    PredictionResponse
)

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


@router.post(
    "/predict-category",
    response_model=PredictionResponse
)
def predict(request: PredictionRequest):

    category = predict_category(
        request.description
    )

    return PredictionResponse(
        category=category
    )