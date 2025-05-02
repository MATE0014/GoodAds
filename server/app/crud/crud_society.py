# ...CRUD functions for Society...
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.society import Society
from app.schemas.society import SocietyCreate, SocietyUpdate

async def create_society(db: AsyncSession, society: SocietyCreate, owner_id: int):
    new_society = Society(**society.dict(), owner_id=owner_id)
    db.add(new_society)
    await db.commit()
    await db.refresh(new_society)
    return new_society

# Read (single)
async def get_society(db: AsyncSession, society_id: int) -> Society | None:
    query = select(Society).filter(Society.id == society_id)
    result = await db.execute(query)
    return result.scalars().first()

# Read (multiple)
async def get_societies(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Society]:
    query = select(Society).offset(skip).limit(limit)
    result = await db.execute(query)
    return list(result.scalars().all())

async def update_society(db: AsyncSession, society_id: int, society_update: SocietyUpdate) -> Society | None:
    query = select(Society).filter(Society.id == society_id)
    result = await db.execute(query)
    db_society = result.scalars().first()
    if not db_society:
        return None
    for field, value in society_update.dict(exclude_unset=True).items():
        setattr(db_society, field, value)
    await db.commit()
    await db.refresh(db_society)
    return db_society

async def delete_society(db: AsyncSession, society_id: int) -> bool:
    query = select(Society).filter(Society.id == society_id)
    result = await db.execute(query)
    db_society = result.scalars().first()
    if not db_society:
        return False
    db.delete(db_society)
    await db.commit()
    return True