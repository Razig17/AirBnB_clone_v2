#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import scoped_session, sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        url = f"mysql+mysqldb://{user}:{passwd}@{host}/{db}"
        self.__engine = create_engine(url, pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            query = self.__session.query(cls).all()
        else:
            query = self.__session.query(State).all() + \
                self.__session.query(City).all() + \
                self.__session.query(User).all() + \
                self.__session.query(Place).all()
        return {f"{obj.__class__.__name__}.{obj.id}": obj
                for obj in query}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and current database session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()
