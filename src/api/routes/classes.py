from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.classes import Class, ClassSchema
from api.utils.database import db

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

    fetched = Class.query.all()
    class_schema = ClassSchema(many=True)
    classes = class_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"classes": classes})
