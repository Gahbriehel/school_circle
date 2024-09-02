from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.teachers import Teacher, TeacherSchema
from api.utils.database import db


teacher_routes = Blueprint("teacher_routes", __name__)


@teacher_routes.route("/", methods=["POST"])
def create_teacher():

    try:
        data = request.get_json()
        teacher_schema = TeacherSchema()
        teacher = teacher_schema.load(data)
        result = teacher_schema.dump(teacher.create())
        return response_with(resp.SUCCESS_201, value={"teacher": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@teacher_routes.route("/", methods=["GET"])
def get_all_teachers():

    fetched = Teacher.query.all()
    teacher_schema = TeacherSchema(many=True)
    teachers = teacher_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"teachers": teachers})
