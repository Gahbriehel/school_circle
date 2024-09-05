from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.student_subject import StudentsSubject
from api.models.schemas import StudentsSubjectSchema
from api.utils.database import db


st_subject = Blueprint("st_subject", __name__)


@st_subject.route("/", methods=["GET"], strict_slashes=False)
def get_all():

    try:
        fetched = StudentsSubject.query.all()
        st_subject_schemas = StudentsSubjectSchema(many=True)
        st_subjects = st_subject_schemas.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"st_subjects": st_subjects})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@st_subject.route("/", methods=["POST"], strict_slashes=False)
def add_sub_student():

    try:
        data = request.get_json()
        st_sub_schema = StudentsSubjectSchema()
        sub_st = st_sub_schema.load(data)
        result = st_sub_schema.dump(sub_st.create())
        return response_with(resp.SUCCESS_201, value={"student": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@st_subject.route("<id>", methods=["DELETE"], strict_slashes=False)
def delete_sub_student(id):

    try:
        sub_st = StudentsSubject.query.get(id)

        if sub_st is None:
            return response_with(
                resp.SERVER_ERROR_404, message="SubjectStudent not found"
            )
        db.session.delete(sub_st)
        db.session.commit()

        return response_with(resp.SUCCESS_204, message="Student-Subject deleted")
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))
