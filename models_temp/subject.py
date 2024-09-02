#!/usr/bin/python3

"""
Subject Model for out School Circle App
"""

from sqlalchemy import Column, String
import models
from models.base_model import BaseModel

class Subject(BaseModel):
    
    """
    Creates the Subject Model for school circle
    """

    if models.storage_t == "db":

        __tablename__ = "subject"

        subject_name = Column(String(128), nullable=False)

    else:
        subject_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initailizer for class
        """
        super().__init__(*args, **kwargs)


        