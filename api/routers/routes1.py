from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import uuid4
import os
import sys

from common.error_handling import ObjectNotFound
from helpers import initiate_logger
from config import get_db
from models import Model1
from schemas import Model1sinput, Model1soutput

router1 = APIRouter(prefix="/models1", tags=["models1"])

logger = initiate_logger("router1")


@router1.post("/", response_model=Model1soutput)
async def create_model1(model: Model1sinput, db: Session = Depends(get_db)):
    '''Crea una instancia de modelo 1 a partir de un nombre dado'''
    m1_example = Model1(name=f"{model.name}")
    db.add(m1_example)
    db.commit()
    db.refresh(m1_example)
    return m1_example


@router1.get("/", response_model=List[Model1soutput])
async def create_model1(db: Session = Depends(get_db)):
    '''Consulta todos los elementos del modelo 1'''
    all_models1 = db.query(Model1).all()
    return all_models1


@router1.get("/{id}", response_model=Model1soutput)
async def create_model1(id: int, db: Session = Depends(get_db)):
    """Consulta todos los elementos del modelo 1"""
    model1n = db.query(Model1).get(id)
    if not model1n:
        raise ObjectNotFound("el modelo no existe")
    return model1n
