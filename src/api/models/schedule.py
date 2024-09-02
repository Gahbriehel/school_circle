from datetime import datetime
from api.utils.database import db
from uuid import uuid4
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema  # type: ignore
from marshmallow import fields

"""
Schedule Management Table
"""


class Schedule(db.Model):
    """
    Object structure for schedule
    """

    __tablename__ = "schedules"
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    day_of_the_week = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.String(20), nullable=False)
    end_time = db.Column(db.String(20), nullable=False)

    def __init__(self, day_of_the_week, start_time, end_time):
        """
        Inits the Schedule Management Table
        """

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()

        self.day_of_the_week = day_of_the_week
        self.start_time = start_time
        self.end_time = end_time

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class ScheduleSchema(SQLAlchemyAutoSchema):
    """
    ScheduleSchema for serializing and deserializing schedule object
    """

    class Meta:
        model = Schedule
        sqla_session = db.session
        load_instance = True

    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    day_of_the_week = fields.Integer()
    start_time = fields.String(required=True)
    end_time = fields.String(required=True)
