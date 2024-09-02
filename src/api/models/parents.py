from datetime import datetime
from api.utils.database import db
from uuid import uuid4
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema  # type: ignore
from marshmallow import fields


"""
Parents Data
"""


class Parent(db.Model):
    """
    Object structure for parent table
    """

    __tablename__ = "parents"
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(15), nullable=True)

    def __init__(self, first_name, last_name, phone_number):

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class ParentSchema(SQLAlchemyAutoSchema):
    """
    Parent schema for serializing and deserializing parent object
    """

    class Meta:
        model = Parent
        sqla_session = db.session
        load_instance = True

    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    phone_number = fields.String()
