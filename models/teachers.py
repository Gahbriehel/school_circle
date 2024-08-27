#!/usr/bin/python3

"""
Teacher Model for out School Circle App
"""

from models.base_model import BaseModel

class Teacher(BaseModel):
    
    """
    Creates the Teacher Model for school circle
    """

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
