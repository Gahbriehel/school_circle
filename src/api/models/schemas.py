from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.utils.database import db
from api.models.classes import ClassName
from api.models.teachers import Teacher
from marshmallow import fields
from api.models.subjects import Subject
from api.models.class_subject import ClassSubject


class TeacherSchema(SQLAlchemyAutoSchema):
    """
    Teacher schema for serializing and deserializing Teacher object
    """

    # from api.models.classes import ClassSchema

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
    class_assigned = fields.Pluck("ClassSchema", "class_name", dump_only=True)
    class_id = fields.String(load_only=True)


class ClassSchema(SQLAlchemyAutoSchema):
    """
    Class schema for serializing and desrializing Class object
    """

    # from api.models.association_tables import ClassSubject

    class Meta:
        model = ClassName
        sqla_session = db.session
        load_instance = True

    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    class_name = fields.String(required=True)
    teachers = fields.List(
        fields.Nested("TeacherSchema", only=["first_name", "last_name", "id"])
    )
    subjects = fields.List(fields.Nested("ClassSubjectSchema", only=["subject"]))


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
    classes = fields.List(fields.Nested("ClassSubjectSchema", only=["class_d"]))


class ClassSubjectSchema(SQLAlchemyAutoSchema):
    """
    Initializes the schema for serializing and deserializing the above object
    """

    class Meta:

        model = ClassSubject
        sqla_session = db.session
        load_instance = True

    class_id = fields.String(required=True, load_only=True)
    subject_id = fields.String(required=True, load_only=True)
    class_d = fields.Pluck("ClassSchema", "class_name", dump_only=True)
    subject = fields.Pluck("SubjectSchema", "subject_name", dump_only=True)
