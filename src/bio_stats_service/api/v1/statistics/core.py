from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def _get_creature_id(creature_type: str):
    if creature_type == "mice":
        return 1
    elif creature_type == "worm":
        return 2


def get_species_lifespan(db: Session, creature_type: str):
    creature_id = _get_creature_id(creature_type)
    query = text(
        """SELECT compounds.name as compound ,s.name as species, MAX(average_lifespan_change) AS max_med_lifespan_change
FROM compounds
         JOIN experiments e on compounds.id = e.compound_id
         JOIN species s on e.species_id = s.id
WHERE e.creature_id = :creature_id
GROUP BY compounds.id, s.name
ORDER BY max_med_lifespan_change DESC
"""
    )
    res = db.execute(query, {"creature_id": creature_id})
    return list(res)
