from fastapi import FastAPI

from api.database import Base, engine
from api.models import Movement
from api.routers.movement import router as movement_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CashApp Management API"
)

app.include_router(movement_router)


@app.get("/")
def root():
    return {
        "message": "CashApp Management API is running."
    }