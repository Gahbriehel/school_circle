#!/usr/bin/python3

"""
Teacher Model for out School Circle App
"""

from datetime import datetime
import enum
from sqlalchemy import Column, Date, Enum, String
import models
from models.base_model import BaseModel



class Gender(enum):
    """
    Initializes a set of values for gender
    """
    male = "M"
    female = "F"


class RelationshipStatus(enum):
    """
    Specifies relationship status
    """

    single = "single"
    married = "married"
    widowed = "widowed"
    divorced = "divorced"
    widower = "widower"


class Teacher(BaseModel):
    
    """
    Creates the Teacher Model for school circle
    """

    if models.storage_t == "db":

        __tablename__ = "teacher"

        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        username = Column(String(128), nullable=False)
        gender = Column(Enum(Gender), nullable=False)
        email = Column(String(128), nullable=False)
        dob = Column(Date, default=datetime.date)
        relationship_status = Column(Enum(RelationshipStatus), default="single")
        nationality = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        street = Column(String(128), nullable=False)
        city = Column(String(128), nullable=False)
        state = Column(String(128), nullable=False)
        country = Column(String(128), nullable=False)
        emergency_contact = Column(String(128), nullable=False)
        phone_number = Column(String(128), nullable=False)

    else:

        first_name = ""
        last_name = ""
        username = ""
        gender = ""
        email = ""
        dob = ""
        relationship_status = ""
        nationality = ""
        password = ""
        street = ""
        city = ""
        state = ""
        country = ""
        emergency_contact = ""
        phone_number = ""
        # subject
        # class/grade

    def __init__(self, *args, **kwargs):
        """
        Class initailizer
        """

        super().__init__(*args, **kwargs)