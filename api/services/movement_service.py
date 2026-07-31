from sqlalchemy.orm import Session

from api.models.movement import Movement
from api.schemas.movement import MovementCreate, MovementUpdate


def create_movement(db: Session, movement: MovementCreate):
    db_movement = Movement(**movement.model_dump())

    db.add(db_movement)
    db.commit()
    db.refresh(db_movement)

    return db_movement


def get_all_movements(db: Session):
    return db.query(Movement).all()


def get_movement_by_id(db: Session, movement_id: int):
    return db.query(Movement).filter(
        Movement.id == movement_id
    ).first()


def update_movement(
    db: Session,
    movement_id: int,
    movement: MovementUpdate
):
    db_movement = get_movement_by_id(db, movement_id)

    if db_movement is None:
        return None

    for key, value in movement.model_dump().items():
        setattr(db_movement, key, value)

    db.commit()
    db.refresh(db_movement)

    return db_movement


def delete_movement(db: Session, movement_id: int):
    db_movement = get_movement_by_id(db, movement_id)

    if db_movement is None:
        return None

    db.delete(db_movement)
    db.commit()

    return db_movement