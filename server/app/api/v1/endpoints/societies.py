# ...societies endpoints will go here...
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud
from app.schemas.society import Society, SocietyCreate, SocietyUpdate
from app.db.session import get_db

router = APIRouter()

# Create Society
@router.post("/societies/", response_model=Society)
def create_society(society_in: SocietyCreate, db: Session = Depends(get_db)):
    society = crud.create_society(db=db, society=society_in)
    return society

# Get Single Society
@router.get("/societies/{society_id}", response_model=Society)
def read_society(society_id: int, db: Session = Depends(get_db)):
    society = crud.get_society(db=db, society_id=society_id)
    if not society:
        raise HTTPException(status_code=404, detail="Society not found")
    return society

# Get Multiple Societies
@router.get("/societies/", response_model=List[Society])
def read_societies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    societies = crud.get_societies(db=db, skip=skip, limit=limit)
    return societies

# Update Society
@router.put("/societies/{society_id}", response_model=Society)
def update_society(society_id: int, society_in: SocietyUpdate, db: Session = Depends(get_db)):
    society = crud.update_society(db=db, society_id=society_id, society_update=society_in)
    if not society:
        raise HTTPException(status_code=404, detail="Society not found")
    return society

# Delete Society
@router.delete("/societies/{society_id}", response_model=dict)
def delete_society(society_id: int, db: Session = Depends(get_db)):
    success = crud.delete_society(db=db, society_id=society_id)
    if not success:
        raise HTTPException(status_code=404, detail="Society not found")
    return {"ok": True}
