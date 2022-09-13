from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "circuit"
    circuitId = Column(Integer, primary_key=True, index=True)
    name     = Column(String, unique=True, index=True)
    location   = Column(String, unique=True, index=True)
    country   = Column(String, unique=True, index=True)
    

