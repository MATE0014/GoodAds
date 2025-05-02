from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.business import Business
from app.schemas.business import BusinessCreate, BusinessUpdate

async def get_business(db: AsyncSession, business_id: int):
    result = await db.execute(select(Business).filter(Business.id == business_id))
    return result.scalars().first()

async def get_businesses(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Business).offset(skip).limit(limit))
    return result.scalars().all()

async def create_business(db: AsyncSession, business: BusinessCreate, owner_id: int):
    db_business = Business(**business.dict(), owner_id=owner_id)
    db.add(db_business)
    await db.commit()
    await db.refresh(db_business)
    return db_business

async def update_business(db: AsyncSession, db_business: Business, business_update: BusinessUpdate):
    for key, value in business_update.dict(exclude_unset=True).items():
        setattr(db_business, key, value)
    await db.commit()
    await db.refresh(db_business)
    return db_business

async def delete_business(db: AsyncSession, db_business: Business):
    await db.delete(db_business)
    await db.commit()
    return db_business
