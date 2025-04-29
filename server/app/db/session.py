from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Convert the standard PostgreSQL URL to use the asyncpg driver
if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Create engine
engine = create_async_engine(DATABASE_URL, connect_args={"ssl":True}, echo=True)

# Create session
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Dependency for FastAPI
async def get_db():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()