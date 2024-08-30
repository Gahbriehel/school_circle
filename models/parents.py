#!/usr/bin/python3

"""
Parents Model for out School Circle App
"""

from sqlalchemy import Column, String
import models
from models.base_model import BaseModel

class Parents(BaseModel):
    
    """
    Creates the Parent Model for school circle
    """

    if models.storage_t == "db":
        __tablename__ = "parents"

        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        phone_number = Column(String(128), nullable=False)
        relationship_with_student = Column(String(128), nullable=False)
    else:
        first_name = ""
        last_name = ""
        phone_number = ""
        relationship_with_student = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Place
        """
        super().__init__(*args, **kwargs)