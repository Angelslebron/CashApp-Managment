from fastapi import FastAPI

from api.database import Base, engine

from api.models import Movement

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CashApp Managment API")


@app.get("/")
def root():
    return {
        "message: CashApp Management API is running."
    }