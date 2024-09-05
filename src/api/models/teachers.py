from datetime import datetime
from api.utils.database import db
from uuid import uuid4
from passlib.hash import pbkdf2_sha256 as sha256


"""
Teachers Data Model
"""


class Teacher(db.Model):
    """
    Object structure for teacher table
    """

    __tablename__ = "teachers"

    # Columns
    id = db.Column(db.String(60), primary_key=True)

    # Timestampss
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

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

    # Relationships
    class_id = db.Column(db.String(60), db.ForeignKey("classes.id"))
    class_assigned = db.relationship("ClassName", back_populates="teachers")

    subjects = db.relationship("SubjectTeacher", back_populates="teacher")

    schedules = db.relationship("Schedule", back_populates="teacher")

    def __init__(
        self, first_name, last_name, email, username, password, class_id=None, **kwargs
    ):
        """
        Initializes a new Teacher instance
        """

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
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
        self.class_id = class_id

    def create(self):
        """
        Adds the Teacher instance to the sesssion and commits it to the database
        """
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_username(cls, username):
        """
        Finds a Teacher by their username
        """
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def generate_hash(password):
        """
        Generates a hashed password
        """
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        """
        Verifies if the provided passsword matches the hashed password
        """
        return sha256.verify(password, hash)
