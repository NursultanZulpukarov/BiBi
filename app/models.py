from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey  # Добавили Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Master(Base):
    __tablename__ = "masters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, unique=True)
    category = Column(String)
    district = Column(String)
    rating = Column(Float)
    phone = Column(String)
    is_active = Column(Boolean, default=True)

    # Связь: один мастер имеет много услуг
    services = relationship("Service", back_populates="owner")

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    master_id = Column(Integer, ForeignKey("masters.id"))
    title = Column(String)
    description = Column(String)
    price = Column(Integer)
    duration_minutes = Column(Integer)
    photo_url = Column(String)

    # Обратная связь
    owner = relationship("Master", back_populates="services")