#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.state import State


class City(BaseModel, Base):
    """ Blue print for creating a city object """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey(State.id), nullable=False)

    state = relationship('State', back_populates='cities')
