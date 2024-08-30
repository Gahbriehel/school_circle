#!/usr/bin/python3

"""
Admin Model for out School Circle App
"""

from models import storage_t
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from hashlib import md5


class Admin(BaseModel, Base):
    """
    Creates the Admin Model for school circle
    """

    if storage_t == "db":
        __tablename__ = "admin"
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        username = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)

    else:
        first_name = ""
        last_name = ""
        username = ""
        password = ""
        email = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Class
        """
        super().__init__(*args, **kwargs)
