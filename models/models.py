from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from config import Base


class Model1(Base):
    __tablename__ = "model1"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    model2 = relationship("Model2")


class Model2(Base):
    __tablename__ = "model2"

    id = Column(Integer, primary_key=True, index=True)
    hobby = Column(String, index=True)
    model1_id = Column(Integer, ForeignKey('model1.id'))
