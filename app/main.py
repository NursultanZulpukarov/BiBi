from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select 
from typing import List, Optional

from .database import get_db
from . import crud, schemas, models

app = FastAPI(title="Bi Bi App API")

# Настройка CORS для фронтендеров
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/masters", response_model=List[schemas.MasterBase])
async def read_masters(
    category: Optional[str] = Query(None, description="Фильтрация по категории (например, 'nails')"),
    db: AsyncSession = Depends(get_db)
):
    masters = await crud.get_masters(db, category=category)
    return masters

@app.get("/services", response_model=List[schemas.ServiceBase])
async def read_services(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Service))
    return result.scalars().all()