from datetime import datetime
from api.utils.database import db
from uuid import uuid4


"""
Subject and Teacher Association table
"""


class SubjectTeacher(db.Model):
    """
    Subject Teachers
    """

    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    teacher_id = db.Column(
        db.String(60), db.ForeignKey("teachers.id"), nullable=False, primary_key=True
    )
    subject_id = db.Column(
        db.String(60), db.ForeignKey("subjects.id"), nullable=False, primary_key=True
    )

    teacher = db.relationship("Teacher", back_populates="subjects")
    subject = db.relationship("Subject", back_populates="teachers")

    def __init__(self, teacher_id=None, subject_id=None):
        """
        Initializes the Subject Teacher Object
        """
        self.created_at = datetime.utcnow()
        self.teacher_id = teacher_id
        self.subject_id - subject_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
