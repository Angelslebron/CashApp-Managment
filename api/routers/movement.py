from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.movement import MovementCreate, MovementResponse
from api.services.movement_service import (
    create_movement,
    get_all_movements,
)

router = APIRouter(
    prefix="/movements",
    tags=["Movements"]
)


@router.post("/", response_model=MovementResponse)
def create(
    movement: MovementCreate,
    db: Session = Depends(get_db)
):
    return create_movement(db, movement)


@router.get("/", response_model=list[MovementResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_movements(db)
from api.schemas.movement import (
    MovementCreate,
    MovementResponse,
    MovementUpdate,
)

from api.services.movement_service import (
    create_movement,
    delete_movement,
    get_all_movements,
    get_movement_by_id,
    update_movement,
)

@router.get("/{movement_id}", response_model=MovementResponse)
def get_by_id(
    movement_id: int,
    db: Session = Depends(get_db)
):
    movement = get_movement_by_id(db, movement_id)

    if movement is None:
        raise HTTPException(
            status_code=404,
            detail="Movement not found"
        )

    return movement


@router.put("/{movement_id}", response_model=MovementResponse)
def update(
    movement_id: int,
    movement: MovementUpdate,
    db: Session = Depends(get_db)
):
    updated = update_movement(
        db,
        movement_id,
        movement
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Movement not found"
        )

    return updated


@router.delete("/{movement_id}")
def delete(
    movement_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_movement(
        db,
        movement_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Movement not found"
        )

    return {
        "message": "Movement deleted successfully"
    }