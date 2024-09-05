from datetime import datetime
from api.utils.database import db
from uuid import uuid4


class StudentsSubject(db.Model):
    """
    Many-to-many relationship for students and subjects
    """

    student_id = db.Column(
        db.String(60), db.ForeignKey("students.id"), primary_key=True
    )
    subject_id = db.Column(
        db.String(60), db.ForeignKey("subjects.id"), primary_key=True
    )

    subject = db.relationship("Subject", back_populates="students")
    student = db.relationship("Student", back_populates="subjects")

    def __init__(self, subject_id=None, student_id=None):
        """
        Initailized the Student and Subject many-to-many relationship
        """

        self.subject_id = subject_id
        self.student_id = student_id

    def create(self):
        db.session.add(self)
        db.session.commit()

        return self
