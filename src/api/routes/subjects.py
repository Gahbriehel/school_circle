from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.subjects import Subject, SubjectSchema
from api.utils.database import db

subject_routes = Blueprint("subject_routes", __name__)


@subject_routes.route("/", methods=["POST"], strict_slashes=False)
def create_subject():

    try:
        data = request.get_json()
        subject_name = data.get("subject_name")

        # Check for uniqueness
        existing_subject = Subject.find_by_subject_name(subject_name)
        if existing_subject:
            return response_with(
                resp.CONFLICT_409,
                value={"message": "Subject name already exists"},
            )
        subject_schema = SubjectSchema()
        subject = subject_schema.load(data)
        result = subject_schema.dump(subject.create())
        return response_with(resp.SUCCESS_201, value={"subject": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@subject_routes.route("/", methods=["GET"], strict_slashes=False)
def get_all_subjects():

    fetched = Subject.query.all()
    subject_schema = SubjectSchema(many=True)
    subjects = subject_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"subjects": subjects})
