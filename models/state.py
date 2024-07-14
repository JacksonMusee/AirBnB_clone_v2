#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                              cascade='all, delete-orphan')

    else:
        @property
        def cities(self):
            """
            Returns the list of City instances with
            state_id equals to the current State.id
            """
            from models import storage

            city_lst = []
            for city in storage.all('City').values:
                if city.state_id == self.id:
                    city_lst.append(city)
            return city_lst
