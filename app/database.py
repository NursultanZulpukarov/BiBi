import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Настройка движка специально для работы с SSL в Neon/asyncpg
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True
)

async_session_local = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session_local() as session:
        yield session