from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.students import Student
from api.models.schemas import StudentSchema
from api.utils.database import db

student_routes = Blueprint("student_routes", __name__)


@student_routes.route("/", methods=["POST"], strict_slashes=False)
def create_student():
    """
    Create a new student record.

    This endpoint handles the creation of a new student by accepting a JSON payload,
    validating and deserializing it using the `StudentSchema`, and then saving the
    student record to the database. If the creation is successful, it returns a
    success response with the created student data. If there is an error during
    processing, it returns an invalid input response.

    Request Body:
        JSON object containing the student details:
        - first_name (str): Required. The first name of the student.
        - last_name (str): Required. The last name of the student.
        - gender (str): The gender of the student.
        - email (str): Required. The email address of the student.
        - dob (str): The date of birth of the student.
        - nationality (str): The nationality of the student.
        - street (str): The street address of the student.
        - city (str): The city of the student.
        - state (str): The state of the student.
        - country (str): The country of the student.
        - phone_number (str): The phone number of the student.
        - username (str): Required. The username for the student.
        - password (str): Required. The password for the student.
        - confirm_password (str): Required. The confirmation of the password.
        - subjects (list): A list of subjects associated with the student.
        - class_id (str): The ID of the class the student belongs to.

    Returns:
        Response: A JSON response with the created student data and a success status code (201),
                  or an error message and an invalid input status code (422) if an exception occurs.
    """

    try:
        data = request.get_json()
        student_schema = StudentSchema()
        student = student_schema.load(data)
        result = student_schema.dump(student.create())
        print("Student created successfully")
        print("received data:", data)
        return response_with(resp.SUCCESS_201, value={"student": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@student_routes.route("/<id>", methods=["GET"], strict_slashes=False)
def get_student_by_id(id):
    """
    Retrieve a student by their ID.

    This endpoint handles GET requests to fetch a student's details based on the provided ID.
    It queries the database for the student with the given ID, serializes the student data using
    the StudentSchema, and returns the serialized data in the response.

    Args:
        id (str): The ID of the student to be retrieved.

    Returns:
        Response: A Flask response object containing the serialized student data and a success status code.
                  If an error occurs, it returns a server error status code and the error message.
    """

    try:
        fetched = Student.query.get(id)
        Student_schema = StudentSchema(many=False)
        student = Student_schema.dump(fetched)
        print("Student fetched by id successfully")
        return response_with(resp.SUCCESS_200, value={"Student": student})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@student_routes.route("/", methods=["GET"], strict_slashes=False)
def get_all_students():
    """
    Retrieve all student records from the database.

    This endpoint handles GET requests to fetch all student records. It queries the database
    for all entries in the `Student` table, serializes the data using `StudentSchema`, and
    returns the serialized data in a JSON response.

    Returns:
        Response: A JSON response containing a list of all students with a success status code.
                  If an error occurs, a JSON response with an error message and server error status code is returned.
    """

    try:
        fetched = Student.query.all()
        student_schema = StudentSchema(many=True)
        students = student_schema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"students": students})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@student_routes.route("/<id>", methods=["PUT"], strict_slashes=False)
def update_student(id):
    """
    Updates an existing student record in the database.

    This endpoint allows updating specific fields of a student record identified by the provided ID.
    If the student does not exist, a 404 error response is returned.
    If the input data is invalid, a 422 error response is returned.

    Parameters:
    id (str): The unique identifier of the student to be updated.

    Request Body (JSON):
    {
        "class_id": "optional, the ID of the class to which the student belongs"
    }

    Returns:
    Response: A JSON response containing the updated student data and a success status code.
    """

    try:
        get_student = Student.query.get(id)

        if not get_student:
            return response_with(resp.SERVER_ERROR_404, message="Student not found")

        data = request.get_json()

        if data:
            if data.get("class_id"):
                get_student.class_id = data["class_id"]

        student_schema = StudentSchema()
        db.session.add(get_student)
        db.session.commit()
        student = student_schema.dump(get_student)
        print("Student updated successfully")
        return response_with(resp.SUCCESS_200, value={"student": student})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@student_routes.route("/<id>", methods=["DELETE"], strict_slashes=False)
def delete_student(id):
    """
    Deletes a student record from the database by student ID.

    This endpoint handles HTTP DELETE requests to remove a student from the database.
    It first attempts to retrieve the student by the provided ID. If the student is not found,
    it returns a 404 response. If the student is found, it deletes the student record and commits
    the transaction to the database, returning a 204 response upon success. If any exception occurs
    during the process, it returns a 500 response with the error message.

    Args:
        id (str): The unique identifier of the student to be deleted.

    Returns:
        Response: A Flask response object with the appropriate HTTP status code and message.
    """

    try:
        student = Student.query.get(id)

        if not student:
            return response_with(resp.SERVER_ERROR_404, message="Student not found")
        db.session.delete(student)
        print("Student deleted successfully")
        student_schema = StudentSchema()
        student = student_schema.dump(student)
        db.session.commit()
        return response_with(resp.SUCCESS_200, value={"student": student})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))
