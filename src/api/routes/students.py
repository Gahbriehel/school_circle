from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.students import Student
from api.models.schemas import StudentSchema
from api.utils.database import db

student_routes = Blueprint("student_routes", __name__)


@student_routes.route("/", methods=["POST"], strict_slashes=False)
def create_student():
    try:
        data = request.get_json()
        student_schema = StudentSchema()
        student = student_schema.load(data)
        result = student_schema.dump(student.create())
        print("received data:", data)
        return response_with(resp.SUCCESS_201, value={"student": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@student_routes.route("/", methods=["GET"], strict_slashes=False)
def get_all_students():

    try:
        fetched = Student.query.all()
        student_schema = StudentSchema(many=True)
        students = student_schema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"students": students})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@student_routes.route("/<id>", methods=["PUT"], strict_slashes=False)
def update_student(id):

    try:
        get_student = Student.query.get(id)

        if not get_student:
            return response_with(resp.SERVER_ERROR_404, message="Student not found")

        data = request.get_json()

        if data:
            if data.get("class_id"):
                get_student.class_id = data["class_id"]

        student_schema = StudentSchema()
        db.session.add(get_student)
        db.session.commit()
        student = student_schema.dump(get_student)
        return response_with(resp.SUCCESS_204, value={"student": student})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@student_routes.route("/<id>", methods=["DELETE"], strict_slashes=False)
def delete_student(id):
    try:
        student = Student.query.get(id)

        if not student:
            return response_with(resp.SERVER_ERROR_404, message="Student not found")
        db.session.delete(student)
        db.session.commit()
        return response_with(resp.SUCCESS_204, messsage="Student successfully deleted")
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))
