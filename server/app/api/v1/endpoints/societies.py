# ...societies endpoints will go here...
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.models import user as UserModel

from app import crud
from app.schemas.society import Society, SocietyCreate, SocietyUpdate
from app.db.session import get_db
from app.core.deps import get_current_user, require_user_type

router = APIRouter()

@router.post("/societies/", response_model=Society)
async def create_society(
    society_in: SocietyCreate,
    db: AsyncSession = Depends(get_db),
    current_user: UserModel.User = Depends(require_user_type("society")),
):
    society = await crud.create_society(db=db, society=society_in, owner_id=current_user.id)
    return society

# Get Single Society (open to all)
@router.get("/societies/{society_id}", response_model=Society)
async def read_society(society_id: int, db: AsyncSession = Depends(get_db)):
    society = await crud.get_society(db=db, society_id=society_id)
    if not society:
        raise HTTPException(status_code=404, detail="Society not found")
    return society

# Get Multiple Societies (open to all)
@router.get("/societies/", response_model=List[Society])
async def read_societies(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    societies = await crud.get_societies(db=db, skip=skip, limit=limit)
    return societies

# Update Society (owner only)
@router.put("/societies/{society_id}", response_model=Society)
async def update_society(
    society_id: int,
    society_in: SocietyUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: UserModel.User = Depends(get_current_user),
):
    db_society = await crud.get_society(db=db, society_id=society_id)
    if not db_society:
        raise HTTPException(status_code=404, detail="Society not found")
    if db_society.owner_id != current_user.id and current_user.user_type != "admin":
        raise HTTPException(status_code=403, detail="You can only update your own society")
    updated = await crud.update_society(db=db, society_id=society_id, society_update=society_in)
    return updated

# Delete Society (owner only)
@router.delete("/societies/{society_id}", response_model=dict)
async def delete_society(
    society_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: UserModel.User = Depends(get_current_user),
):
    db_society = await crud.get_society(db=db, society_id=society_id)
    if not db_society:
        raise HTTPException(status_code=404, detail="Society not found")

    if db_society.owner_id != current_user.id and current_user.user_type != "admin":
        raise HTTPException(status_code=403, detail="Only society owners or admins can delete societies")

    await crud.delete_society(db=db, society_id=society_id)
    return {"ok": True}