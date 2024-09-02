#!/usr/bin/python3

"""
Schedule Model for out School Circle App
"""

import datetime
from sqlalchemy import Column, DateTime, Integer
import models
from models.base_model import BaseModel

class Schedule(BaseModel):
    
    """
    Creates the Schedule Model for school circle
    """


    if models.storage_t == "db":

        __tablename__  = "schedule"

        day_of_the_week = Column(Integer, nullable=False)
        start_time = Column(DateTime, default=datetime.utcnow)
        end_time = Column(DateTime, default=datetime.utcnow)
    else:
        day_of_the_week = 0
        start_time = ""
        end_time = ""


    def __init__(self, *args, **kwargs):
        """
        Initializes the class
        """
        super().__init__(*args, **kwargs)

