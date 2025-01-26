"""
This module contains the SQLAlchemy model for the Property table.
"""
from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_address = Column(String, index=True)
    class_description = Column(String)
    estimated_market_value = Column(Float)
    building_use = Column(String)
    building_square_feet = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
