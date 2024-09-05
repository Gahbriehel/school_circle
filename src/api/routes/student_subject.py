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

    fetched = StudentsSubject.query.all()
    st_subject_schemas = StudentsSubjectSchema(many=True)
    st_subjects = st_subject_schemas.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"st_subjects": st_subjects})


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
