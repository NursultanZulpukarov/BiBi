from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Beauty Marketplace API")

masters = [
    {
        "id": 1, 
        "name": "Diana Neylova", 
        "username": "diana.nails", 
        "category": "nails", 
        "district": "Bishkek", 
        "rating": 4.9
    },
    {
        "id": 2, 
        "name": "Studio Glow", 
        "username": "glow.studio", 
        "category": "spa", 
        "district": "Bishkek", 
        "rating": 4.7
    },
]

class Master(BaseModel):
    id: int
    name: str
    username: str
    category: str
    district: str
    rating: float

@app.get("/masters", response_model=List[Master])
async def get_masters():
    """
    Возвращает список всех бьюти-мастеров.
    """
    return masters