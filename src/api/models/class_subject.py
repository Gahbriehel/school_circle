from datetime import datetime
from uuid import uuid4
from api.utils.database import db


class ClassSubject(db.Model):
    """
    Represents the many-to-many relationship between Class and Subject
    """

    __tablename__ = "class_subject"

    # composite primary key using class_id and subject_id
    class_id = db.Column(db.String(60), db.ForeignKey("classes.id"), primary_key=True)
    subject_id = db.Column(
        db.String(60), db.ForeignKey("subjects.id"), primary_key=True
    )

    # unique identifier for the relationship
    id = db.Column(db.String(60), nullable=False, unique=True)

    # Timestamps
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    # Relationships
    class_d = db.relationship("ClassName", back_populates="subjects")
    subject = db.relationship("Subject", back_populates="classes")

    def __init__(self, class_id=None, subject_id=None):
        """
        Initializes the many-to-many rel between class and subject
        """

        self.id = str(uuid4())  # Generates a unique ID for the relationship
        self.updated_at = datetime.utcnow()
        self.created_at = datetime.utcnow()

        self.class_id = class_id
        self.subject_id = subject_id

    def create(self):
        """
        Adds the class Subject instance to the seeson and commits
        """
        db.session.add(self)
        db.session.commit()
        return self
