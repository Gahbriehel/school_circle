#!/usr/bin/python3

"""
New engine for the database
"""

import os
import models
from models.admin import Admin
from models.base_model import Base
from models.classes import Class
from models.parents import Parents
from models.students import Student
from models.schedule import Schedule
from models.subject import Subject
from models.teachers import Teacher
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {
            "Admin": Admin,
            "Classes": Class,
            "Parents": Parents,
            "Student": Student,
            "Subject": Subject,
            "Schedule": Schedule,
            "teachers": Teacher
}

class DBStorage:

    """
    New database engine for our School Circle Project
    to connect to MySQL
    """
    
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize the database
        """

        from urllib.parse import quote_plus

        usr = os.getenv("SCH_CIR_MYSQL_USER")
        passwd = quote_plus(os.getenv("SCH_CIR_MYSQL_PWD"))
        host = os.getenv("SCH_CIR_MYSQL_HOST")
        db = os.getenv("SCH_CIR_DB")
        env = os.getenv("SCH_CIR_ENV")

        uri = f"mysql+mysqldb://{usr}:{passwd}@{host}:3306/{db}"

        self.__engine = create_engine(uri, pool_pre_ping=True)

        if os.getenv("SCH_CIR_ENV") == "test":
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """
        Queries the current database
        """
        table_names = [
            "admin",
            "classes",
            "parents",
            "student",
            "subject",
            "schdules",
            "teachers"
        ]

        dictionary = {}
        if cls is None:

            for name in table_names:
                result = self.__session.query(classes[name]).all()

                for obj in result:
                    key = obj.to_dict()['__class__'] + '.' + obj.id
                    dictionary[key] = obj
        else:
            result = self.__session.query(classes[cls]).all()

            for obj in result:
                key = obj.to_dict()['__class__'] + '.' + obj.id
                dictionary[key] = obj
        
        return dictionary

    def new(self, obj):
        """
        Adds a new object to the current database session
        """

        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes from a current database session
        """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database
        """

        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        call remove() mthod on the private session attribute
        """
        self.___session.remove()

    def get(self, cls, id):
        """
        Returns the object bases on the class name and its ID, or
        None if not found
        """

        if cls not in classes.values():
            return None
        
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
            
        return None
    
    def count(self, cls=None):
        """
        count the number of objects in storage
        """

        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
