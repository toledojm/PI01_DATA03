from weakref import proxy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Circuit(Base):
    __tablename__ = "circuit"

    circuitId = Column(Integer, primary_key=True, index=True)
    name     = Column(String, unique=True, index=True)
    location   = Column(String, unique=True, index=True)
    country   = Column(String, unique=True, index=True)


class Driver(Base):
    __tablename__ = "driver"

    driverId     = Column(Integer, primary_key=True, index=True)
    driverRef    = Column(String, unique=True, index=True)
    nationality  = Column(String, index=True)
    forename     = Column(String, index=True)
    surname      = Column(String, unique=True, index=True)

    race=relationship("Race")


class Result(Base):
    __tablename__ = "result"

    resultId      = Column(Integer, primary_key=True, index=True)  
    raceId        = Column(Integer,ForeignKey("race.raceId"), unique=True, index=True)  
    driverId      = Column(Integer,ForeignKey("driver.driverId"), unique=True, index=True) 
    constructorId = Column(Integer,ForeignKey("cosntructor.constructorId"), unique=True, index=True)  
    number        = Column(String, unique=True, index=True) 
    positionOrder = Column(Integer, index=True)  
    points        = Column(float, index=True)
    laps          = Column(Integer, index=True)  
    rank          = Column(String, index=True)
    statusId      = Column(Integer, index=True)

    diver = relationship("Driver")
    constructor = relationship("Constructor")
    race=relationship("Race")


class Race(Base):
    __tablename__ = "race"

    raceId     = Column(Integer, primary_key=True, index=True)  
    year       = Column(Integer, index=True)
    round      = Column(Integer, index=True)
    circuitId  = Column(Integer,ForeignKey("circuit.circuitId"), unique=True, index=True)  
    name       = Column(String, index=True) 

    circuit=relationship("Circuit")


class Constructor(Base):
    __tablename__ = "constructor"
    constructorId   = Column(Integer, primary_key=True, index=True)  
    constructorRef  = Column(Integer, index=True)  
    name            = Column(String, index=True)
    nationality     = Column(String, index=True)

    result = relationship("Result")
