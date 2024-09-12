from flask import Blueprint, request
from werkzeug.security import check_password_hash
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.students import Student
from api.models.schemas import StudentSchema
from api.utils.database import db

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/login", methods=["POST"], strict_slashes=False)
def login():
    try:
        # Get data from request
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Find student by email
        student = Student.query.filter_by(email=email).first()

        if student and check_password_hash(student.password, password):
            # Serialize student data
            student_schema = StudentSchema()
            result = student_schema.dump(student)

            # Return successful login response
            return response_with(resp.SUCCESS_200, value={"student": result})

        else:
            # Invalid credentials
            return response_with(resp.UNAUTHORIZED_401, message="Invalid email or password")

    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))
