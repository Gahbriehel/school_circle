#!/usr/bin/python3

"""
Admin Model for out School Circle App
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Admin(BaseModel, Base):
    
    """
    Creates the Admin Model for school circle
    """

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)

