#!/usr/bin/python3

"""
Student Model for out School Circle App
"""

from models.base_model import BaseModel

class Student(BaseModel):
    
    """
    Creates the Student Model for school circle
    """

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
