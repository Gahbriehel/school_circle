#!/usr/bin/python3

"""
This module defines a base class
for all models in our school_circle app
"""

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String
from os import getenv

Base = declarative_base()


class BaseModel:
    """
    Base Model that will be derived by all ther classes
    """

    if getenv("SCH_CIR_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Instantiates a new model
        """

        if not kwargs or (
            "updated_at" not in kwargs
            and "created_at" not in kwargs
            and "__class__" not in kwargs
        ):

            from models import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.__dict__.update(kwargs)

        else:
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            del kwargs["__class__"]
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Returns a string representation of the instance
        """

        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        dictionary = self.__dict__

        if "_sa_instance_state" in self.__dict__:
            del dictionary["_sa_instance_state"]

        return "[{}] ({}) {}".format(cls, self.id, dictionary)

    def save(self):
        """
        Updates and saves to file
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Convert instance into dict format
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__": (str(type(self)).split(".")[-1]).split("'")[0]})
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        if "_sa_instance_state" in self.__dict__:
            del dictionary["_sa_instance_state"]

        return dictionary

    def delete(self):
        """
        Delete current instance from storage
        """

        from models import storage

        storage.delete(self)
