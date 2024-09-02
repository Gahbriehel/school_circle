from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.students import Student, StudentSchema
from api.utils.database import db

student_routes = Blueprint("student_routes", __name__)


@student_routes.route("/", methods=["POST"], strict_slashes=False)
def create_student():
    try:
        data = request.get_json()
        student_schema = StudentSchema()
        student = student_schema.load(data)
        result = student_schema.dump(student.create())
        return response_with(resp.SUCCESS_201, value={"student": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@student_routes.route("/", methods=["GET"], strict_slashes=False)
def get_all_students():

    fetched = Student.query.all()
    student_schema = StudentSchema(many=True)
    students = student_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"students": students})
