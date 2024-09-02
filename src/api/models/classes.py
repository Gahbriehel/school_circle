from datetime import datetime
from api.utils.database import db
from uuid import uuid4
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema  # type: ignore
from marshmallow import fields

"""
Class Data
"""


class Class(db.Model):
    """
    Object structure for class table
    """

    __tablename__ = "classes"
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    class_name = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, class_name):
        """
        Initiates the class table
        """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()

        self.class_name = class_name

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class ClassSchema(SQLAlchemyAutoSchema):
    """
    Class schema for serializing and desrializing Class object
    """

    class Meta:
        model = Class
        sqla_session = db.session
        load_instance = True

    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

    class_name = fields.String(required=True)
