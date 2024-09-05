from datetime import datetime
from api.utils.database import db
from uuid import uuid4
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema  # type: ignore
from marshmallow import fields


"""
Student Data
"""


class Student(db.Model):
    """
    Object structure for student table
    """

    __tablename__ = "students"
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    dob = db.Column(db.DateTime, nullable=True)
    street = db.Column(db.String(128), nullable=True)
    city = db.Column(db.String(128), nullable=True)
    nationality = db.Column(db.String(64), nullable=True)
    country = db.Column(db.String(128), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    state = db.Column(db.String(128), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)
    password = db.Column(db.String(128), nullable=False)

    subjects = db.relationship("StudentsSubject", back_populates="student")

    class_id = db.Column(db.String(60), db.ForeignKey("classes.id"))
    class_d = db.relationship("ClassName", back_populates="students")

    def __init__(
        self, first_name, last_name, email, username, password, class_id=None, **kwargs
    ):

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = self.generate_hash(password)

        self.gender = kwargs.get("gender")
        self.dob = kwargs.get("dob")
        self.nationality = kwargs.get("nationality")
        self.street = kwargs.get("street")
        self.city = kwargs.get("city")
        self.state = kwargs.get("state")
        self.country = kwargs.get("country")
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
