from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.subjects import Subject
from api.models.schemas import SubjectSchema
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

    try:
        fetched = Subject.query.all()
        subject_schema = SubjectSchema(many=True)
        subjects = subject_schema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"subjects": subjects})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@subject_routes.route("/<id>", methods=["PUT"], strict_slashes=False)
def update_subject(id):

    try:
        subject = Subject.query.get(id)

        if not subject:
            return response_with(resp.SERVER_ERROR_404, message="Subject not found")
        data = request.get_json()

        db.session.add(subject)
        db.session.commit()

        subject_schema = SubjectSchema()
        result = subject_schema.dump(subject)
        return response_with(resp.SUCCESS_200, value={"subject": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@subject_routes.route("/<id>", methods=["DELETE"], strict_slashes=False)
def delete_subject(id):

    try:
        subject = Subject.query.get(id)

        if not subject:
            return response_with(resp.SERVER_ERROR_404, message="Subject not found")

        db.session.delete(subject)
        db.session.commit()
        return response_with(resp.SUCCESS_204, message="Subject deleted")

    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))
