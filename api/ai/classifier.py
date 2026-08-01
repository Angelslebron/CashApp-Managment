import os

import joblib


BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "movement_model.pkl"
)


model = joblib.load(MODEL_PATH)


def predict_category(description: str) -> str:

    prediction = model.predict([description])

    return prediction[0]