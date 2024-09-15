from datetime import datetime
from api.utils.database import db
from uuid import uuid4


"""
Class Data Model
"""


class ClassName(db.Model):
    """
    Represents the class table structure in the school circle application
    """

    __tablename__ = "classes"

    # Column definitions
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    class_name = db.Column(db.String(128), unique=True, nullable=False)

    # Relationships
    teachers = db.relationship("Teacher", back_populates="class_assigned", uselist=True)
    subjects = db.relationship("ClassSubject", back_populates="class_d")
    schedules = db.relationship("Schedule", back_populates="class_d")
    students = db.relationship("Student", back_populates="class_d")

    def __init__(self, class_name):
        """
        Initializes the className instance
        """
        self.id = str(uuid4())  # Generates a unique ID for the class
        self.updated_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        self.class_name = class_name

    def create(self):
        """
        Adds the className instance to the session and commits it
        """
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get_all_students(cls, id):

        get_class = cls.query.get_id(id)
        students = get_class.students

        return students

    @classmethod
    def get_class_id(cls, class_name):

        get_class = cls.query.filter_by(class_name=class_name).first()

        return get_class.id
