from datetime import datetime
from api.utils.database import db
from uuid import uuid4


"""
Parents Data Model
"""


class Parent(db.Model):
    """
    Represents the structure of the parents table in the school Circle application.
    """

    __tablename__ = "parents"

    # Column definitions
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(15), nullable=True)

    # Relationships
    students = db.relationship("ParentStudent", back_populates="parent")

    def __init__(self, first_name, last_name, phone_number):
        """
        Initializes a Parent instance
        """

        self.id = str(uuid4())  # Generate a unique ID for the parent model
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def create(self):
        """
        Adds the Parent instance to the session and commits it to database
        """
        db.session.add(self)
        db.session.commit()
        return self
