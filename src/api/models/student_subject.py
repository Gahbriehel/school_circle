from datetime import datetime
from api.utils.database import db
from uuid import uuid4


class StudentsSubject(db.Model):
    """
    Many-to-many relationship for students and subjects
    """
