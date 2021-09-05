from typing import Optional

from pydantic import BaseModel
from enum import Enum


class Experiment(BaseModel):
    compound: str
    species: str
    max_med_lifespan_change: Optional[float]

    class Config:
        orm_mode = True


class CreatureType(str, Enum):
    MICE = "mice"
    WORM = "worm"
