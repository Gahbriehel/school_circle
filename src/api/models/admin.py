from datetime import datetime
from api.utils.database import db
from uuid import uuid4
from passlib.hash import pbkdf2_sha256 as sha256


"""
Admin data model for school circle
"""


class Admin(db.Model):
    """
    Creates the Admin Model for school circle
    """

    # Column definitions
    __tablename__ = "admin"
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, first_name, last_name, username, email, password, id=None):
        if not id:
            self.id = str(uuid4())  # Genrates a new UUID if none is provided
        self.updated_at = datetime.utcnow()
        self.created_at = datetime.utcnow()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = self.generate_hash(password)

    def create(self):
        """Add the new admin to the session and commit"""
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_username(cls, username):
        """Find admin by username"""
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_email(cls, email):
        """
        Finds a student by their email
        """
        return cls.query.filter_by(email=email).first()


    # Gabe add

    @staticmethod
    def generate_hash(password):
        """
        Generates a hashed password
        """
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        """
        Verifies if the provided password matches the hashed password
        """
        return sha256.verify(password, hash)
