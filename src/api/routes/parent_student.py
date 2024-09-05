from flask import Blueprint, request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.parent_student import ParentStudent
from api.models.schemas import ParentStudentSchema
from api.utils.database import db

parent_student_routes = Blueprint("parent_student_routes", __name__)


@parent_student_routes.route("/", methods=["POST"], strict_slashes=False)
def create_parent_student():
    try:
        data = request.get_json()
        parent_student_schema = ParentStudentSchema()
        parent_student_data = parent_student_schema.load(data)

        result = parent_student_schema.dump(parent_student_data.create())

        return response_with(resp.SUCCESS_201, value={"parent_student": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@parent_student_routes.route("/", methods=["GET"], strict_slashes=False)
def get_all_parent_students():

    try:
        fetched = ParentStudent.query.all()
        parent_student_schema = ParentStudentSchema(many=True)
        parent_students = parent_student_schema.dump(fetched)
        return response_with(
            resp.SUCCESS_200, value={"parent_students": parent_students}
        )
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@parent_student_routes.route("/<id>", methods=["DELETE"], strict_slashes=False)
def delete_parent_student(parent_id, student_id):
    try:
        parent_student = ParentStudent.query.get(id)
        if not parent_student:
            return response_with(
                resp.SERVER_ERROR_404, message="Parent Student not found"
            )

        db.session.delete(parent_student)
        db.session.commit()
        return response_with(
            resp.SUCCESS_204, message="Parent Student deleted successfully"
        )
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))
