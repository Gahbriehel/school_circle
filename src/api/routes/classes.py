from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.classes import ClassName
from api.utils.database import db
from api.models.schemas import ClassSchema

class_routes = Blueprint("class_routes", __name__)


@class_routes.route("/", methods=["POST"], strict_slashes=False)
def create_class():

    try:
        data = request.get_json()
        class_schema = ClassSchema()
        class_data = class_schema.load(data)
        result = class_schema.dump(class_data.create())
        return response_with(resp.SUCCESS_201, value={"class": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@class_routes.route("/", methods=["GET"], strict_slashes=False)
def get_all_classes():

    fetched = ClassName.query.all()
    class_schema = ClassSchema(many=True)
    classes = class_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"classes": classes})


@class_routes.route("/<id>", methods=["PUT"], strict_slashes=False)
def update_class(id):

    try:
        data = request.get_json()
        get_class = ClassName.query.get(id)

        if data.get("teacher_id"):
            get_class.teacher_id = data["teacher_id"]

        db.session.add(get_class)
        db.session.commit()
        class_schema = ClassSchema()
        classes = class_schema.dump(get_class)
        return response_with(resp.SUCCESS_204, value={"class": classes})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_FILED_NAME_SENT_422)


@class_routes.route("/<id>", methods=["DELETE"], strict_slashes=False)
def delete_class(id):

    try:
        get_class = ClassName.query.get(id)
        db.session.delete(get_class)
        db.session.commit()
        return response_with(resp.SUCCESS_204)
    except Exception as e:
        return response_with(resp.SERVER_ERROR_500)


@class_routes.route("/<id>", methods=["GET"], strict_slashes=False)
def get_class_by_id(id):

    try:
        fetched = ClassName.query.get(id)
        class_schema = ClassSchema(many=False)
        class_data = class_schema.dump(fetched)
        print("Class fetched by id successfully")
        return response_with(resp.SUCCESS_200, value={"Class": class_data})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))
