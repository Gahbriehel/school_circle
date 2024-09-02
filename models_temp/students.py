#!/usr/bin/python3

"""
Student Model for out School Circle App
"""

from datetime import datetime
import enum

from sqlalchemy import Column, Date, Enum, String
import models
from models.base_model import BaseModel



class Gender(enum.Enum):
    """
    Declares an enum set of values for my code
    """
    male = "M"
    female = "F"

class Student(BaseModel):
    
    """
    Creates the Student Model for school circle
    """

    if models.storage_t == "db":

        __tablename__ = "student"

        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        username = Column(String(50), nullable=False)
        gender = Column(Enum(Gender), nullable=False)
        email = Column(String(128), nullable=False)
        dob = Column(Date, default=datetime.date)
        nationality = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        street = Column(String(128), nullable=False)
        city = Column(String(128), nullable=False)
        state = Column(String(128), nullable=False)
        country = Column(String, nullable=False)

    else:
        first_name = ""
        last_name = ""
        username = ""
        gender = ""
        email = ""
        dob = ""
        nationality = ""
        password = ""
        street = ""
        city = ""
        state = ""
        country = ""
    # class/grade


    def __init__(self, *args, **kwargs):
        """
        Initializer for program
        """
        super().__init__(*args, **kwargs)


