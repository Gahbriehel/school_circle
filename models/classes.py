#!/usr/bin/python3

"""
Class Model for out School Circle App
"""

import models
from models.base_model import BaseModel
from sqlalchemy import Column, String

class Class(BaseModel):
    
    """
    Creates the Class Model for school circle
    """

    if models.storage_t == "db":
        __tablename__ = "classes"

        class_name = Column(String(128), nullable=False)
    else:
        class_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Class
        """
        super().__init__(*args, **kwargs)

