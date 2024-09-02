from datetime import datetime
from api.utils.database import db
from uuid import uuid4
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema  # type: ignore
from marshmallow import fields


"""
Teachers Data
"""


class Teacher(db.Model):

    __tablename__ = "teachers"
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.String(10), nullable=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    dob = db.Column(db.DateTime, nullable=True)
    relationship_status = db.Column(db.String(64), nullable=True)
    nationality = db.Column(db.String(64), nullable=True)
    street = db.Column(db.String(128), nullable=True)
    city = db.Column(db.String(128), nullable=True)
    state = db.Column(db.String(128), nullable=True)
    country = db.Column(db.String(128), nullable=True)
    emergency_contact = db.Column(db.String(15), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)

    password = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, first_name, last_name, email, username, password, **kwargs):

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = self.generate_hash(password)

        self.gender = kwargs.get("gender")
        self.dob = kwargs.get("dob")
        self.relationship_status = kwargs.get("relationship_status")
        self.nationality = kwargs.get("nationality")
        self.street = kwargs.get("street")
        self.city = kwargs.get("city")
        self.state = kwargs.get("state")
        self.country = kwargs.get("country")
        self.emergency_contact = kwargs.get("emergency_contact")
        self.phone_number = kwargs.get("phone_number")

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class TeacherSchema(SQLAlchemyAutoSchema):
    """
    Teacher schema for serializing and deserializing Teacher object
    """

    class Meta:
        model = Teacher
        sqla_session = db.session
        load_instance = True

    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    gender = fields.String()
    email = fields.Email(required=True)
    dob = fields.Date()
    relationship_status = fields.String()
    nationality = fields.String()
    street = fields.String()
    city = fields.String()
    state = fields.String()
    country = fields.String()
    emergency_contact = fields.String()
    phone_number = fields.String()
    username = fields.String(required=True)
    password = fields.String(load_only=True)
