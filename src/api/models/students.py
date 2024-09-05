from datetime import datetime
from api.utils.database import db
from uuid import uuid4
from passlib.hash import pbkdf2_sha256 as sha256


"""
Student Data Model
"""


class Student(db.Model):
    """
    Represents the student table in the database
    """

    __tablename__ = "students"

    # Column definitions
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

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

    # Relationships
    subjects = db.relationship("StudentsSubject", back_populates="student")
    class_id = db.Column(db.String(60), db.ForeignKey("classes.id"))
    class_d = db.relationship("ClassName", back_populates="students")
    parents = db.relationship("ParentStudent", back_populates="student")

    def __init__(
        self, first_name, last_name, email, username, password, class_id=None, **kwargs
    ):
        """
        Initializes a new student instance
        """

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = self.generate_hash(password)

        # Optional fields
        self.gender = kwargs.get("gender")
        self.dob = kwargs.get("dob")
        self.nationality = kwargs.get("nationality")
        self.street = kwargs.get("street")
        self.city = kwargs.get("city")
        self.state = kwargs.get("state")
        self.country = kwargs.get("country")
        self.phone_number = kwargs.get("phone_number")

    def create(self):
        """
        Adds the student instance to the session and commits it to the database
        """
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_username(cls, username):
        """
        Finds a student by their username
        """
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def generate_hash(password):
        """
        Generates a hashed password using pbkdf2_sha256
        """
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        """
        Verifies a password against a hashed value
        """
        return sha256.verify(password, hash)
