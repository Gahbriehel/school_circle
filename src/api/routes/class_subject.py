from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.class_subject import ClassSubject
from api.models.schemas import ClassSubjectSchema
from api.utils.database import db

class_subject_r = Blueprint("class_subject_r", __name__)


@class_subject_r.route("/", methods=["GET"], strict_slashes=False)
def get_all_class_sub():

    try:
        fecthed = ClassSubject.query.all()
        class_sub_schema = ClassSubjectSchema(many=True)
        class_sub = class_sub_schema.dump(fecthed)
        return response_with(resp.SUCCESS_200, value={"class_subjects": class_sub})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@class_subject_r.route("/", methods=["POST"], strict_slashes=False)
def create_class_sub():

    try:
        data = request.get_json()
        class_sub_schema = ClassSubjectSchema()
        class_sub_data = class_sub_schema.load(data)
        result = class_sub_schema.dump(class_sub_data.create())
        return response_with(resp.SUCCESS_201, value={"class_subjects": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@class_subject_r.route("/<id>", methods=["PUT"], strict_slashes=False)
def update_class_sub(id):
    try:
        data = request.get_json()
        class_sub = ClassSubject.query.get(id)
        if not class_sub:
            return response_with(
                resp.SERVER_ERROR_404, message="class subject not found"
            )
        class_sub_schema = ClassSubjectSchema()
        class_sub = class_sub_schema.load(data)
        db.session.commit()
        result = class_sub_schema.dump(class_sub)
        return response_with(resp.SUCCESS_200, value={"class_subject": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422, message=str(e))


@class_subject_r.route("/<id>", methods=["DELETE"], strict_slashes=False)
def delete_class_sub(id):
    try:
        class_sub = ClassSubject.query.get(id)
        if not class_sub:
            return response_with(
                resp.SERVER_ERROR_404, message="ClassSubject not found"
            )

        db.session.delete(class_sub)
        db.session.commit()
        return response_with(
            resp.SUCCESS_204, message="ClassSubject deleted successfully"
        )
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))
