from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.parents import Parent
from api.models.schemas import ParentSchema
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

    try:
        fetched = Parent.query.all()
        parent_schema = ParentSchema(many=True)
        parents = parent_schema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"parents": parents})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@parent_routes.route("/<id>", methods=["PUT"], strict_slashes=False)
def update_parent(id):

    try:
        data = request.get_json()
        parent = Parent.query.get(id)

        if not parent:
            return response_with(resp.SERVER_ERROR_404, message="parent not found")

        parent_schema = ParentSchema()
        parent = parent_schema.load(data)
        db.session.commit()
        result = parent_schema.dump(parent)

        return response_with(resp.SUCCESS_200, value={"parent": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422, message=str(e))


@parent_routes.route("/<id>", methods=["DELETE"], strict_slashes=False)
def delete_parent(id):

    try:
        parent = Parent.query.get(id)

        if not parent:
            return response_with(resp.SERVER_ERROR_404, message="parent not found")

        db.session.delete(parent)
        db.session.commit()

        return response_with(resp.SUCCESS_204, message="Parent deleted successfully")
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, messsage=str(e))
