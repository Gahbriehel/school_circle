from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.utils.database import db
from api.models.classes import ClassName
from api.models.teachers import Teacher
from marshmallow import fields
from api.models.subjects import Subject
from api.models.class_subject import ClassSubject
from api.models.subject_teacher import SubjectTeacher
from api.models.schedule import Schedule
from api.models.students import Student
from api.models.student_subject import StudentsSubject
from api.models.parent_student import ParentStudent
from api.models.parents import Parent
from api.models.admin import Admin


"""
Schemas for deserializing and serializing all data models defined from JSON to database and vice versa
"""


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
    updated_at = fields.String()
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
    confirm_password = fields.String(load_only=True)
    class_assigned = fields.Pluck("ClassSchema", "class_name", dump_only=True)
    class_id = fields.String(load_only=True)
    subjects = fields.List(fields.Nested("SubjectTeacherSchema", only=["subject"]))
    schedules = fields.List(fields.Nested("ScheduleSchema", exclude=["teacher"]))


class ClassSchema(SQLAlchemyAutoSchema):
    """
    Class schema for serializing and desrializing Class object
    """

    class Meta:
        model = ClassName
        sqla_session = db.session
        load_instance = True

    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.String()
    class_name = fields.String(required=True)
    teachers = fields.List(
        fields.Nested("TeacherSchema", only=["first_name", "last_name", "id"])
    )
    subjects = fields.List(fields.Nested("ClassSubjectSchema", only=["subject"]))
    schedules = fields.List(fields.Nested("ScheduleSchema"))
    students = fields.List(
        fields.Nested("StudentSchema", only=["first_name", "last_name", "dob", "gender", "street", "city", "state", "country", "phone_number"])
    )


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
    teachers = fields.List(fields.Nested("SubjectTeacherSchema", only=["teacher"]))
    schedules = fields.List(fields.Nested("ScheduleSchema"))
    students = fields.List(fields.Nested("StudentsSubjectSchema", only=["student"]))


class ClassSubjectSchema(SQLAlchemyAutoSchema):
    """
    ClassSubject schema for serializing and deserializing ClassSubejct object
    """

    class Meta:

        model = ClassSubject
        sqla_session = db.session
        load_instance = True

    class_id = fields.String(required=True, load_only=True)
    subject_id = fields.String(required=True, load_only=True)
    class_d = fields.Pluck("ClassSchema", "class_name", dump_only=True)
    subject = fields.Pluck("SubjectSchema", "subject_name", dump_only=True)
    id = fields.String(dump_only=True)
    created_at = fields.String(dump_only=True)
    updated_at = fields.String()


class SubjectTeacherSchema(SQLAlchemyAutoSchema):
    """
    Subject Teacher Schema for many-to-many relationship
    """

    class Meta:
        """
        Meta description for outer class
        """

        model = SubjectTeacher
        sqla_session = db.session
        load_instance = True

    teacher_id = fields.String(required=True, load_only=True)
    subject_id = fields.String(required=True, load_only=True)

    teacher = fields.List(
        fields.Nested("TeacherSchema", only=["first_name", "last_name"])
    )
    subject = fields.List(fields.Nested("SubjectSchema", only=["subject_name"]))


class ScheduleSchema(SQLAlchemyAutoSchema):
    """
    ScheduleSchema for serializing and deserializing schedule object
    """

    class Meta:
        model = Schedule
        sqla_session = db.session
        load_instance = True

    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.String()
    day_of_the_week = fields.Integer()
    start_time = fields.String(required=True)
    end_time = fields.String(required=True)
    class_id = fields.String(load_only=True, required=True)
    class_d = fields.Pluck("ClassSchema", "class_name", dump_only=True)
    subject_id = fields.String(load_only=True, required=True)
    subject = fields.Pluck("SubjectSchema", "subject_name", dump_only=True)
    teacher_id = fields.String(load_only=True, required=True)
    teacher = fields.Nested(
        "TeacherSchema", only=["first_name", "last_name", "id"], dump_only=True
    )


class StudentSchema(SQLAlchemyAutoSchema):
    """
    Student schema for serializing and deserializing Student object
    """

    class Meta:
        model = Student
        sqla_session = db.session
        load_instance = True

    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.String()
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    gender = fields.String()
    email = fields.Email(required=True)
    dob = fields.Date()
    nationality = fields.String()
    street = fields.String()
    city = fields.String()
    state = fields.String()
    country = fields.String()
    phone_number = fields.String()
    username = fields.String(required=True)
    password = fields.String(load_only=True)
    confirm_password = fields.String(load_only=True)
    subjects = fields.List(fields.Nested("StudentsSubjectSchema", only=["subject"]))
    class_id = fields.String(load_only=True)
    class_d = fields.Pluck("ClassSchema", "class_name", dump_only=True)
    parents = fields.List(fields.Nested("ParentStudentSchema", only=["student"]))


class StudentsSubjectSchema(SQLAlchemyAutoSchema):
    """
    StudentsSubject schema for many-to-many relationship
    """

    class Meta:
        model = StudentsSubject
        sqla_session = db.session
        load_instance = True

    student_id = fields.String(load_only=True, required=True)
    subject_id = fields.String(load_only=True, required=True)
    subject = fields.Nested("SubjectSchema", only=["subject_name"])
    student = fields.Nested("StudentSchema", only=["first_name", "last_name"])
    id = fields.String(dump_only=True)
    created_at = fields.String(dump_only=True)
    updated_at = fields.String()


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
    students = fields.List(fields.Nested("ParentStudentSchema", only=["student"]))


class ParentStudentSchema(SQLAlchemyAutoSchema):
    """
    ParentStudent schema for many-to-many relationship
    """

    class Meta:
        model = ParentStudent
        sqla_session = db.session
        load_instance = True

    parent_id = fields.String(load_only=True, required=True)
    student_id = fields.String(load_only=True, required=True)

    student = fields.Nested("StudentSchema", only=["first_name", "last_name"])
    parent = fields.Nested(
        "ParentSchema", only=["first_name", "last_name", "phone_number"]
    )
    id = fields.String(dump_only=True)
    created_at = fields.String(dump_only=True)
    updated_at = fields.String()


class AdminSchema(SQLAlchemyAutoSchema):
    """
    Admin schema for sserializing and deserializinf Admin object
    """

    class Meta:
        model = Admin
        sqla_session = db.session
        load_instance = True

    id = fields.String(dump_only=True)
    username = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)
    created_at = fields.DateTime(dump_only=True)
    password = fields.String(load_only=True)
    updated_at = fields.String()
