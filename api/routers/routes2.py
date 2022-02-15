from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import os
import sys

from helpers import initiate_logger
from config import get_db
from models import Model1, Model2
from schemas import Model2sinput, Model2soutput

router2 = APIRouter(prefix="/models2", tags=["models2"])

logger = initiate_logger("router2")


@router2.post("/", response_model=Model2soutput)
async def create_model1(model: Model2sinput, db: Session = Depends(get_db)):
    m1_example: Model1 = db.query(Model1).get(model.model1_id)
    m2_example = Model2(hobby=f"{model.hobby}")
    m1_example.model2.append(m2_example)
    db.add(m2_example)
    db.commit()
    db.refresh(m1_example)
    return m2_example


@router2.get("/", response_model=List[Model2soutput])
async def create_model1(db: Session = Depends(get_db)):
    all_models2 = db.query(Model2).all()
    return all_models2
