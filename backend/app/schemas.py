"""
This module contains the Pydantic models for the FastAPI application.
"""
from pydantic import BaseModel
from typing import Optional, List


class Property(BaseModel):
    id: int
    full_address: Optional[str]
    class_description: Optional[str]
    estimated_market_value: Optional[float]
    building_use: Optional[str]
    building_square_feet: Optional[float]
    latitude: Optional[float]
    longitude: Optional[float]

    class Config:
        orm_mode = True


class PropertyPaginationResponse(BaseModel):
    total: int
    properties: List[Property]
