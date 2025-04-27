# ...CRUD functions for Society...

from sqlalchemy.orm import Session
from app.models.society import Society
from app.schemas.society import SocietyCreate, SocietyUpdate

def create_society(db: Session, society: SocietyCreate) -> Society:
    db_society = Society(**society.dict())
    db.add(db_society)
    db.commit()
    db.refresh(db_society)
    return db_society

# Read (single)
def get_society(db: Session, society_id: int) -> Society | None:
    return db.query(Society).filter(Society.id == society_id).first()

# Read (multiple)
def get_societies(db: Session, skip: int = 0, limit: int = 100) -> list[Society]:
    return db.query(Society).offset(skip).limit(limit).all()

def update_society(db: Session, society_id: int, society_update: SocietyUpdate) -> Society | None:
    db_society = db.query(Society).filter(Society.id == society_id).first()
    if not db_society:
        return None
    for field, value in society_update.dict(exclude_unset=True).items():
        setattr(db_society, field, value)
    db.commit()
    db.refresh(db_society)
    return db_society

def delete_society(db: Session, society_id: int) -> bool:
    db_society = db.query(Society).filter(Society.id == society_id).first()
    if not db_society:
        return False
    db.delete(db_society)
    db.commit()
    return True
