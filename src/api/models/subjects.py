from datetime import datetime
from api.utils.database import db
from uuid import uuid4
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema  # type: ignore
from marshmallow import fields

"""
Subject Data
"""


class Subject(db.Model):
    """
    Object structure for Subject table
    """

    __tablename__ = "subjects"
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    subject_name = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, subject_name):
        """
        Inits the subject object
        """
        self.subject_name = subject_name
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_subject_name(cls, subject_name):
        return cls.query.filter_by(subject_name=subject_name).first()


class SubjectSchema(SQLAlchemyAutoSchema):
    """
    Subject schema for serializing and deserializing Subject object
    """

    class Meta:
        model = Subject
        sqla_session = db.session
        load_instance = True

    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    subject_name = fields.String(required=True)
