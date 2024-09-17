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

    day_of_the_week = db.Column(db.Integer, nullable=False)  # accepts number from 1 - 7
    start_time = db.Column(db.String(20), nullable=False)  # accepts string exp: "18:00"
    end_time = db.Column(db.String(20), nullable=False)  # accepts string exp: "19:00"

    # Foreign key relationships
    class_id = db.Column(
        db.String(60), db.ForeignKey("classes.id")
    )  # The class the schdule belongs to
    class_d = db.relationship(
        "ClassName", back_populates="schedules"
    )  # Class data shows the name of the class

    subject_id = db.Column(
        db.String(60), db.ForeignKey("subjects.id")
    )  # subject_id receives the subject id
    subject = db.relationship(
        "Subject", back_populates="schedules"
    )  # shows the subject name

    teacher_id = db.Column(
        db.String(60), db.ForeignKey("teachers.id")
    )  # receives the teacher's id
    teacher = db.relationship(
        "Teacher", back_populates="schedules"
    )  # shows the teacher for this schedule


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
