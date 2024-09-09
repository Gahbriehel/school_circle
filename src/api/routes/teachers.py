from datetime import datetime
from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.teachers import Teacher
from api.utils.database import db
from api.models.schemas import TeacherSchema


teacher_routes = Blueprint("teacher_routes", __name__)



@teacher_routes.route("/", methods=["POST"], strict_slashes=False)
def create_teacher():

    try:
        print(request.get_data())
        data = request.get_json()
        teacher_schema = TeacherSchema()
        teacher = teacher_schema.load(data)
        result = teacher_schema.dump(teacher.create())
        print("received data:", data)
        return response_with(resp.SUCCESS_201, value={"teacher": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@teacher_routes.route("/<id>", methods=["GET"], strict_slashes=False)
def get_teacher_by_id(id):
    try:
        fetched = Teacher.query.get(id)
        teacher_schema = TeacherSchema(many=False)
        teacher = teacher_schema.dump(fetched)
        print ("teacher fetched by id successfully")
        return response_with(resp.SUCCESS_200, value={"teacher": teacher})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))

@teacher_routes.route("/", methods=["GET"], strict_slashes=False)
def get_all_teachers():

    try:
        fetched = Teacher.query.all()
        teacher_schema = TeacherSchema(many=True)
        teachers = teacher_schema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"teachers": teachers})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@teacher_routes.route("/<id>", methods=["DELETE"], strict_slashes=False)
def delete_teacher(id):

    try:
        get_teacher = Teacher.query.get(id)
        db.session.delete(get_teacher)
        db.session.commit()
        
        
        print (f"Teacher with id {get_teacher} deleted successfully")
        teacher_schema = TeacherSchema()
        teacher = teacher_schema.dump(get_teacher)
        return response_with(resp.SUCCESS_204, value={"teacher": teacher})
    except Exception as e:
        return response_with(resp.SERVER_ERROR_500)


@teacher_routes.route("/<id>", methods=["PUT"], strict_slashes=False)
def update_teacher(id):

    try:
        data = request.get_json()
        get_teacher = Teacher.query.get(id)

        if not get_teacher:
            return response_with(resp.SERVER_ERROR_404, message="Teacher not found")

        if data:
            data["updated_at"] = str(datetime.utcnow())

        teacher_schema = TeacherSchema()
        get_teacher = teacher_schema.load(data)
        db.session.commit()
        teacher = teacher_schema.dump(get_teacher)
        return response_with(resp.SUCCESS_204, value={"teacher": teacher})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
