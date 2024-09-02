from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.parents import Parent, ParentSchema
from api.utils.database import db

parent_routes = Blueprint("parent_routes", __name__)


@parent_routes.route("/", methods=["POST"], strict_slashes=False)
def create_parent():
    try:
        data = request.get_json()
        parent_schema = ParentSchema()
        parent = parent_schema.load(data)
        result = parent_schema.dump(parent.create())
        return response_with(resp.SUCCESS_201, value={"parent": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@parent_routes.route("/", methods=["GET"], strict_slashes=False)
def get_all_parents():

    fetched = Parent.query.all()
    parent_schema = ParentSchema(many=True)
    parents = parent_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"parents": parents})
