from datetime import datetime
from api.utils.database import db
from uuid import uuid4


class ParentStudent(db.Model):
    """
    Represents the many-to-many relationship between Parent and Student
    """

    __tablename__ = "parent_student"

    # Composite primary key using parent_id and student_id
    parent_id = db.Column(db.String(60), db.ForeignKey("parents.id"), primary_key=True)
    student_id = db.Column(
        db.String(60), db.ForeignKey("students.id"), primary_key=True
    )

    # Unique identifier for the relationship
    id = db.Column(db.String(60), nullable=False, unique=True)

    # Timestamps
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    # Relationships
    student = db.relationship("Student", back_populates="parents")
    parent = db.relationship("Parent", back_populates="students")

    def __init__(self, parent_id=None, student_id=None):
        """
        Initializes the Parent Student many-to-many relationship
        """

        self.id = str(uuid4())  # Generates a unique ID for the relationship
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.parent_id = parent_id
        self.student_id = student_id

    def create(self):
        """
        Adds the ParentStudent instance to the session and commit
        """
        db.session.add(self)
        db.session.commit()
        return self
