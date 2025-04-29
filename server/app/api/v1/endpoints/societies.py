# ...societies endpoints will go here...
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.models import user as UserModel

from app import crud
from app.schemas.society import Society, SocietyCreate, SocietyUpdate
from app.db.session import get_db
from app.core.deps import get_current_user

router = APIRouter()

@router.post("/societies/", response_model=Society)
def create_society(
    society_in: SocietyCreate,
    db: Session = Depends(get_db),
    current_user: UserModel.User = Depends(get_current_user),
):
    if current_user.user_type != "society":
        raise HTTPException(status_code=403, detail="Only society users can create societies")
    society = crud.create_society(db=db, society=society_in, owner_id=current_user.id)
    return society

# Get Single Society (open to all)
@router.get("/societies/{society_id}", response_model=Society)
def read_society(society_id: int, db: Session = Depends(get_db)):
    society = crud.get_society(db=db, society_id=society_id)
    if not society:
        raise HTTPException(status_code=404, detail="Society not found")
    return society

# Get Multiple Societies (open to all)
@router.get("/societies/", response_model=List[Society])
def read_societies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    societies = crud.get_societies(db=db, skip=skip, limit=limit)
    return societies

# Update Society (owner only)
@router.put("/societies/{society_id}", response_model=Society)
def update_society(
    society_id: int,
    society_in: SocietyUpdate,
    db: Session = Depends(get_db),
    current_user: UserModel.User = Depends(get_current_user),
):
    db_society = crud.get_society(db=db, society_id=society_id)
    if not db_society:
        raise HTTPException(status_code=404, detail="Society not found")
    if db_society.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only update your own society")
    updated = crud.update_society(db=db, society_id=society_id, society_update=society_in)
    return updated

# Delete Society (owner only)
@router.delete("/societies/{society_id}", response_model=dict)
def delete_society(
    society_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel.User = Depends(get_current_user),
):
    db_society = crud.get_society(db=db, society_id=society_id)
    if not db_society:
        raise HTTPException(status_code=404, detail="Society not found")
    if db_society.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only delete your own society")
    crud.delete_society(db=db, society_id=society_id)
    return {"ok": True}
