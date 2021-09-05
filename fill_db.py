import csv
import os

from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.bio_stats_service.external import models
from src.bio_stats_service.external.database import SessionLocal

MICE_DATA_PATH = os.path.join("test_data", "mice_data.csv")
WORMS_DATA_PATH = os.path.join("test_data", "worms_data.csv")


def _create_creatures_types(db: Session):
    mice = models.Creature(name="mice")
    worm = models.Creature(name="worm")
    db.add(mice)
    db.add(worm)
    db.commit()
    db.refresh(mice)
    db.refresh(worm)
    return mice.id, worm.id


def _fill_unique_tables(db: Session, data, model_cls):
    for value in data:
        model = model_cls(name=value)
        db.add(model)
        db.commit()


def _fill_experiment_data(db: Session, experiment_data):
    for sample in experiment_data:
        compound_name, species_name, lifespan_change, ref, creature_id = sample

        compound = (
            db.query(models.Compound)
            .filter(models.Compound.name == compound_name)
            .first()
        )

        species = (
            db.query(models.Species).filter(models.Species.name == species_name).first()
        )

        experiment = models.Experiment(
            average_lifespan_change=lifespan_change if lifespan_change else None,
            reference=ref,
            creature_id=creature_id,
            compound_id=compound.id,  # type: ignore
            species_id=species.id,  # type: ignore
        )

        db.add(experiment)
        db.commit()


def _get_creature_data_from_csv(csv_path, creature_id):
    creature_data = []
    with open(csv_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # ignore headers
        for line in reader:
            creature_data.append(line + [creature_id])
    return creature_data


if __name__ == "__main__":
    db = SessionLocal()
    try:
        mice_id, worm_id = _create_creatures_types(db)
    except IntegrityError:
        logger.warning("Creatures are already in database")
        exit(0)

    mice_data = _get_creature_data_from_csv(MICE_DATA_PATH, mice_id)
    worms_data = _get_creature_data_from_csv(WORMS_DATA_PATH, worm_id)
    all_data = mice_data + worms_data
    unique_compounds = set((row[0] for row in all_data))
    unique_species = set((row[1] for row in all_data))
    _fill_unique_tables(db, unique_compounds, models.Compound)
    _fill_unique_tables(db, unique_species, models.Species)
    _fill_experiment_data(db, all_data)
