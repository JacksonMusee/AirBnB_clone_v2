#!/usr/bin/python3
"""A module for database storage engine"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    """An instance of this class class is an instance of db"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates DBStorage"""
        env = getenv("HBNB_ENV")
        usr = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(usr, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls=None):
        """
        Query current database session and return a dict of
        all objects depending of the class name
        """
        objects = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            for obj in self.__session.query().all():
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Adds obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the db and create a session (Thread safe)"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """Closes the current database session"""
        self.__session.remove()
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
