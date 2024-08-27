#!/usr/bin/python3

"""
Admin Model for out School Circle App
"""

from models.base_model import BaseModel

class Admin(BaseModel):
    
    """
    Creates the Admin Model for school circle
    """

    first_name = ""
    last_name = ""
    username = ""
    password = ""
    email = ""

