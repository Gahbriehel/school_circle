from datetime import datetime
from uuid import uuid4
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.utils.database import db


class ClassSubject(db.Model):

    __tablename__ = "class_subject"

    class_id = db.Column(db.String(60), db.ForeignKey("classes.id"), primary_key=True)
    subject_id = db.Column(
        db.String(60), db.ForeignKey("subjects.id"), primary_key=True
    )

    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    class_d = db.relationship("ClassName", back_populates="subjects")
    subject = db.relationship("Subject", back_populates="classes")

    def __init__(self, class_id=None, subject_id=None):
        """
        Initializes the many-to-many rel between class and subject
        """

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()

        self.class_id = class_id
        self.subject_id = subject_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
