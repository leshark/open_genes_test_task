from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ....external.database import get_db
from .core import get_species_lifespan
from .schemes import CreatureType, Experiment

stats_router = APIRouter(prefix="/api/v1/stats", tags=["stats"])


@stats_router.get(
    "/get_lifespan",
    summary="Получить максимальные значения изменения продолжительности жизни для обоих видов",  # noqa E501
    response_model=List[Experiment],
)
async def get_lifespan_view(creature_type: CreatureType, db: Session = Depends(get_db)):
    res = get_species_lifespan(db, creature_type)
    return res
