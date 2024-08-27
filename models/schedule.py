#!/usr/bin/python3

"""
Schedule Model for out School Circle App
"""

from models.base_model import BaseModel

class Schedule(BaseModel):
    
    """
    Creates the Schedule Model for school circle
    """

    day_of_the_week = 0
    start_time = ""
    end_time = ""
