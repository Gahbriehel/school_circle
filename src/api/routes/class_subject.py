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

    fecthed = ClassSubject.query.all()
    class_sub_schema = ClassSubjectSchema(many=True)
    class_sub = class_sub_schema.dump(fecthed)
    return response_with(resp.SUCCESS_200, value={"class_subjects": class_sub})


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
