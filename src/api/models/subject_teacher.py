from datetime import datetime
from api.utils.database import db
from uuid import uuid4


"""
Subject and Teacher Data Model
"""


class SubjectTeacher(db.Model):
    """
    Represents the relationship between subjects and teachers
    """

    __tablename__ = "subject_teacher"

    # Column definitions
    id = db.Column(db.String(60), nullable=False, unique=True, primary_key=True)

    # Timestamp
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    # Composite keys
    teacher_id = db.Column(db.String(60), db.ForeignKey("teachers.id"), nullable=False)
    subject_id = db.Column(db.String(60), db.ForeignKey("subjects.id"), nullable=False)

    # Relationships
    teacher = db.relationship("Teacher", back_populates="subjects")
    subject = db.relationship("Subject", back_populates="teachers")

    def __init__(self, teacher_id=None, subject_id=None):
        """
        Initializes the Subject Teacher Object
        """
        self.created_at = datetime.utcnow()
        print("After created_at")
        self.updated_at = datetime.utcnow()
        print("After updated_at")
        self.id = str(uuid4())
        print("After str_at")
        self.teacher_id = teacher_id
        print("After teacher_id")
        self.subject_id = subject_id
        print("After subject_id")

    def create(self):
        # Adds the Subject Teacher instance to the session and commits to it
        db.session.add(self)
        db.session.commit()
        return self
