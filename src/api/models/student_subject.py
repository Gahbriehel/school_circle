from datetime import datetime
from api.utils.database import db
from uuid import uuid4

"""
Students and Subject many-to-many data model
"""


class StudentsSubject(db.Model):
    """
    Represents the many-to-many relationship between students and subjects
    """

    __tablename__ = "student_subject"

    # Column definitions
    student_id = db.Column(
        db.String(60), db.ForeignKey("students.id"), primary_key=True
    )
    subject_id = db.Column(
        db.String(60), db.ForeignKey("subjects.id"), primary_key=True
    )
    id = db.Column(db.String(60), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    # Relationships
    subject = db.relationship("Subject", back_populates="students")
    student = db.relationship("Student", back_populates="subjects")

    def __init__(self, subject_id=None, student_id=None):
        """
        Initailized the many-to-many relationship between students and subjects
        """

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.id = str(uuid4())
        self.subject_id = subject_id
        self.student_id = student_id

    def create(self):
        """
        Addss the Students Subject instance to the session and commits it
        """
        db.session.add(self)
        db.session.commit()

        return self
