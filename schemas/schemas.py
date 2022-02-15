from pydantic import BaseModel
from typing import Optional, Any, List
from uuid import UUID


class Model1sinput(BaseModel):
    name: str


class Model2sfiltered(BaseModel):
    id: int
    hobby: str

    class Config:
        orm_mode = True


class Model1soutput(Model1sinput):
    id: int
    model2: List[Model2sfiltered]

    class Config:
        orm_mode = True


class Model2sinput(BaseModel):
    model1_id: int
    hobby: str


class Model2soutput(Model2sinput):
    id: int

    class Config:
        orm_mode = True
