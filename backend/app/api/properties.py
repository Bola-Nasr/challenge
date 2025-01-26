"""
The API routes for the properties endpoint.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from ..models.property import Property
from .. import schemas, database

router = APIRouter()


def apply_filters(
    query,
    full_address: Optional[str],
    class_description: Optional[str],
    min_market_value: Optional[float],
    max_market_value: Optional[float],
    building_use: Optional[str],
    min_square_feet: Optional[float],
    max_square_feet: Optional[float],
):
    """
    Apply filters to the query based on the provided parameters.
    :param query:
    :param full_address:
    :param class_description:
    :param min_market_value:
    :param max_market_value:
    :param building_use:
    :param min_square_feet:
    :param max_square_feet:
    :return:
    """
    if full_address:
        query = query.filter(Property.full_address.contains(full_address))
    if class_description:
        query = query.filter(Property.class_description.contains(class_description))
    if min_market_value:
        query = query.filter(Property.estimated_market_value >= min_market_value)
    if max_market_value:
        query = query.filter(Property.estimated_market_value <= max_market_value)
    if building_use:
        query = query.filter(Property.building_use.contains(building_use))
    if min_square_feet:
        query = query.filter(Property.building_square_feet >= min_square_feet)
    if max_square_feet:
        query = query.filter(Property.building_square_feet <= max_square_feet)
    return query


def apply_sorting(query, sort_by: Optional[str]):
    """
    Apply sorting to the query based on the provided parameter.
    :param query:
    :param sort_by:
    :return:
    """
    if sort_by:
        if sort_by == "market_value_asc":
            query = query.order_by(Property.estimated_market_value.asc())
        elif sort_by == "market_value_desc":
            query = query.order_by(Property.estimated_market_value.desc())
        elif sort_by == "square_feet_asc":
            query = query.order_by(Property.building_square_feet.asc())
        elif sort_by == "square_feet_desc":
            query = query.order_by(Property.building_square_feet.desc())
    return query


@router.get("/api/properties", response_model=schemas.PropertyPaginationResponse)
def get_properties(
    skip: int = 0,
    limit: int = 20,
    full_address: Optional[str] = None,
    class_description: Optional[str] = None,
    min_market_value: Optional[float] = None,
    max_market_value: Optional[float] = None,
    building_use: Optional[str] = None,
    min_square_feet: Optional[float] = None,
    max_square_feet: Optional[float] = None,
    sort_by: Optional[str] = None,
    db: Session = Depends(database.get_db),
):
    """
    Get a paginated list of properties based on the provided parameters.
    :param skip:
    :param limit:
    :param full_address:
    :param class_description:
    :param min_market_value:
    :param max_market_value:
    :param building_use:
    :param min_square_feet:
    :param max_square_feet:
    :param sort_by:
    :param db:
    :return:
    """
    query = db.query(Property)
    query = apply_filters(
        query,
        full_address,
        class_description,
        min_market_value,
        max_market_value,
        building_use,
        min_square_feet,
        max_square_feet,
    )
    query = apply_sorting(query, sort_by)

    total_count = query.count()
    properties = query.offset(skip).limit(limit).all()

    return {"total": total_count, "properties": properties}
