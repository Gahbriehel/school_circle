from datetime import datetime
from api.utils.database import db
from uuid import uuid4


"""
Subject Data Model
"""


class Subject(db.Model):
    """
    Represents the Subject table in the database
    """

    __tablename__ = "subjects"

    # Column definition
    id = db.Column(db.String(60), primary_key=True)

    # TimeStamps
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    # Relationships
    subject_name = db.Column(db.String(128), unique=True, nullable=False)
    classes = db.relationship("ClassSubject", back_populates="subject")
    teachers = db.relationship("SubjectTeacher", back_populates="subject")
    schedules = db.relationship("Schedule", back_populates="subject")
    students = db.relationship("StudentsSubject", back_populates="subject")

    def __init__(self, subject_name):
        """
        Initializes a new Subject instance
        """
        self.subject_name = subject_name
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def create(self):
        """
        Adds the Subject instance to the session and commits to the database
        """
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_subject_name(cls, subject_name):
        """
        Finds a Subject by its name
        """
        return cls.query.filter_by(subject_name=subject_name).first()
