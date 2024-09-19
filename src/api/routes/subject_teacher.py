from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.subject_teacher import SubjectTeacher
from api.models.schemas import SubjectTeacherSchema
from api.utils.database import db

subject_teacher_r = Blueprint("subject_teacher_r", __name__)


@subject_teacher_r.route("/", methods=["GET"], strict_slashes=False)
def get_all_teachers_subject():

    try:
        fecthed = SubjectTeacher.query.all()
        subject_teacher_schema = SubjectTeacherSchema(many=True)
        sub_teacher = subject_teacher_schema.dump(fecthed)
        return response_with(resp.SUCCESS_200, value={"subject_teacher": sub_teacher})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@subject_teacher_r.route("/", methods=["POST"], strict_slashes=False)
def create_sub_teacher():

    try:
        data = request.get_json()
        print(data)
        subject_teacher_schema = SubjectTeacherSchema()
        print("Before loading")
        subject_teacher = subject_teacher_schema.load(data)
        print("After loading")
        result = subject_teacher_schema.dump(subject_teacher.create())
        print("Creation of object")
        return response_with(resp.SUCCESS_201, value={"subject_teacher": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@subject_teacher_r.route("/<id>", methods=["PUT"], strict_slashes=False)
def update_subject_teacher(id):
    try:
        data = request.get_json()
        subject_teacher = SubjectTeacher.query.get(id)
        if not subject_teacher:
            return response_with(
                resp.SERVER_ERROR_404, message="class subject not found"
            )
        subject_teacher_schema = SubjectTeacherSchema()
        subject_teacher = subject_teacher_schema.load(data)
        db.session.commit()
        result = subject_teacher_schema.dump(subject_teacher)
        return response_with(resp.SUCCESS_200, value={"subject_teacher": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422, message=str(e))


@subject_teacher_r.route("<id>", methods=["DELETE"], strict_slashes=False)
def delete_class_sub(id):
    try:
        subject_teacher = SubjectTeacher.query.get(id)
        if not subject_teacher:
            return response_with(
                resp.SERVER_ERROR_404, message="SubjectTeacher not found"
            )

        db.session.delete(subject_teacher)
        db.session.commit()
        return response_with(
            resp.SUCCESS_204, message="SubjectTeacher deleted successfully"
        )
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))
