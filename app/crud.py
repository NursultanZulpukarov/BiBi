from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from . import models

async def get_masters(db: AsyncSession, category: str = None):
    # Добавляем .options(selectinload(...)), чтобы подтянуть услуги
    query = select(models.Master).options(selectinload(models.Master.services))
    
    if category:
        query = query.filter(models.Master.category == category)
    
    result = await db.execute(query)
    return result.scalars().all()