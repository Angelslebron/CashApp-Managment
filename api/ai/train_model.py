import os

import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


BASE_DIR = os.path.dirname(__file__)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "training_data.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "movement_model.pkl"
)


def train():

    data = pd.read_csv(DATASET_PATH)

    X = data["description"]
    y = data["category"]

    model = Pipeline([
        ("vectorizer", CountVectorizer()),
        ("classifier", MultinomialNB())
    ])

    model.fit(X, y)

    joblib.dump(
        model,
        MODEL_PATH
    )

    print("Model trained successfully.")
    print(f"Model saved at: {MODEL_PATH}")


if __name__ == "__main__":
    train()