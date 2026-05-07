from pydantic import BaseModel
from typing import List, Optional

class ServiceBase(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: int
    duration_minutes: int
    photo_url: Optional[str] = None

    class Config:
        from_attributes = True

class MasterBase(BaseModel):
    id: int
    name: str
    username: str
    category: str
    district: str
    rating: float
    phone: str
    is_active: bool
    # Теперь каждый мастер будет возвращать список своих услуг
    services: List[ServiceBase] = []

    class Config:
        from_attributes = True