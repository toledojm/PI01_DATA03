from pydantic import BaseModel


class CircuitBase(BaseModel):
    circuitId = int
    name     = str
    location   = str
    country   = str


class User(CircuitBase):
    circuitId = int
    name     = str
    location   = str
    country   = str

    class Config:
        orm_mode = True
