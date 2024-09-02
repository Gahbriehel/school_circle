from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.admin import Admin, AdminSchema
from api.utils.database import db


admin_routes = Blueprint("admin_routes", __name__)


@admin_routes.route("/", methods=["POST"])
def create_admin():

    try:
        data = request.get_json()
        admin_schema = AdminSchema()
        admin = admin_schema.load(data)
        result = admin_schema.dump(admin.create())
        return response_with(resp.SUCCESS_201, value={"admin": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@admin_routes.route("/", methods=["GET"])
def get_admins_list():
    fetched = Admin.query.all()
    admin_schema = AdminSchema(many=True)
    admins = admin_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"admins": admins})
