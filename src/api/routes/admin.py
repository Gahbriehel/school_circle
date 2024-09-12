from datetime import datetime
from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.admin import Admin
from api.models.schemas import AdminSchema
from api.utils.database import db


admin_routes = Blueprint("admin_routes", __name__)


# TODO always update the updated_at key for any update to models made (PUT)

@admin_routes.route("/login", methods=["POST"], strict_slashes=False)
def login():
    """ """
    try:

        data = request.get_json()
        get_admin = Admin.find_by_email(data["email"])

        if not get_admin and not data:
            return response_with(
                resp.SERVER_ERROR_404, value={"message", "user not found"}
            )
        else:
            hash_verify = Admin.verify_hash(data["password"], get_admin.password)

            if not hash_verify:
                return response_with(
                    resp.UNAUTHORIZED_403, value={"message": "wrong password"}
                )
        admin_schema = AdminSchema()
        admin = admin_schema.dump(get_admin)
        return response_with(resp.SUCCESS_200, value={"admin": admin})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)




@admin_routes.route("/", methods=["POST"], strict_slashes=False)
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


@admin_routes.route("/", methods=["GET"], strict_slashes=False)
def get_admins_list():
    fetched = Admin.query.all()
    admin_schema = AdminSchema(many=True)
    admins = admin_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"admins": admins})


@admin_routes.route("/<id>", methods=["PUT"], strict_slashes=False)
def update_admin(id):
    try:
        data = request.get_json()
        admin = Admin.query.get(id)

        if not admin:
            return response_with(resp.SERVER_ERROR_404, message="Admin not found")

        if data:
            data["updated_at"] = datetime.utcnow()

        admin_schema = AdminSchema()
        admin = admin_schema.load(data)
        db.session.commit()
        result = admin_schema.dump(admin)
        return response_with(resp.SUCCESS_200, value={"admin": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422, message=str(e))


@admin_routes.route("/<id>", methods=["DELETE"], strict_slashes=False)
def delete_admin(id):

    try:

        admin = Admin.query.get(id)

        if not admin:
            return response_with(resp.SERVER_ERROR_404, message="Admin not found")

        db.session.delete(admin)
        db.session.commit()
        return response_with(resp.SUCCESS_204, message="Admin deleted")
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))
