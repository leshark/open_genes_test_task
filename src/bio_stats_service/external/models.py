from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Creature(Base):
    __tablename__ = "creatures"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)


class Compound(Base):
    __tablename__ = "compounds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)


class Species(Base):
    __tablename__ = "species"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True, index=True)
    average_lifespan_change = Column(Float, nullable=True)
    reference = Column(Integer)

    creature_id = Column(Integer, ForeignKey("creatures.id"))
    compound_id = Column(Integer, ForeignKey("compounds.id"))
    species_id = Column(Integer, ForeignKey("species.id"))

    compounds = relationship("Compound")
