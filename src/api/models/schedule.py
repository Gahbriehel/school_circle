from datetime import datetime
from api.utils.database import db
from uuid import uuid4

"""
Schedule Data Model
"""


class Schedule(db.Model):
    """
    Represents the structure of the schdules table for managing class shcedule
    """

    __tablename__ = "schedules"

    # Column definitions
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    day_of_the_week = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.String(20), nullable=False)
    end_time = db.Column(db.String(20), nullable=False)

    # Foreign key relationships
    class_id = db.Column(db.String(60), db.ForeignKey("classes.id"))
    class_d = db.relationship("ClassName", back_populates="schedules")

    subject_id = db.Column(db.String(60), db.ForeignKey("subjects.id"))
    subject = db.relationship("Subject", back_populates="schedules")

    teacher_id = db.Column(db.String(60), db.ForeignKey("teachers.id"))
    teacher = db.relationship("Teacher", back_populates="schedules")

    def __init__(
        self,
        day_of_the_week,
        start_time,
        end_time,
        class_id=None,
        subject_id=None,
        teacher_id=None,
    ):
        """
        Initializes a Schedule instance with provided details
        """

        self.id = str(uuid4())  # Generates a unique ID for the schedule
        self.created_at = datetime.utcnow()

        self.day_of_the_week = day_of_the_week
        self.start_time = start_time
        self.end_time = end_time
        self.class_id = class_id
        self.subject_id = subject_id
        self.teacher_id = teacher_id

    def create(self):
        """
        Adds the schedule instance to the session and commits it
        """
        db.session.add(self)
        db.session.commit()
        return self
