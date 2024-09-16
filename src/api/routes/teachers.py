from datetime import datetime
from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.teachers import Teacher
from api.utils.database import db
from api.models.schemas import TeacherSchema


teacher_routes = Blueprint("teacher_routes", __name__)


@teacher_routes.route("/login", methods=["POST"], strict_slashes=False)
def login():
    """ """
    try:

        data = request.get_json()
        get_teacher = Teacher.find_by_email(data["email"])

        if not get_teacher and not data:
            return response_with(
                resp.SERVER_ERROR_404, value={"message", "user not found"}
            )
        else:
            hash_verify = Teacher.verify_hash(data["password"], get_teacher.password)

            if not hash_verify:
                return response_with(
                    resp.UNAUTHORIZED_403, value={"message": "wrong password"}
                )
        teacher_schema = TeacherSchema()
        teacher = teacher_schema.dump(get_teacher)
        return response_with(resp.SUCCESS_200, value={"Teacher": teacher})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@teacher_routes.route("/", methods=["POST"], strict_slashes=False)
def create_teacher():
    """
    Create a new teacher by processing the incoming JSON data.

    This endpoint handles the creation of a new teacher object using the TeacherSchema for validation and deserialization.
    It expects a JSON payload with the teacher's details. If the data is valid, a new teacher is created and a success response
    with the created teacher's details is returned. In case of any exceptions during the process, an error response with status
    code 422 for invalid input is returned.

    Returns:
        Response: A JSON response containing the created teacher's details and a success status code 201 if successful.
                  An error response with status code 422 if there is an exception during processing.
    """

    try:
        print(request.get_data())
        data = request.get_json()
        teacher_schema = TeacherSchema()
        teacher = teacher_schema.load(data)
        result = teacher_schema.dump(teacher.create())
        print("Teacher created successfully")
        print("received data:", data)
        return response_with(resp.SUCCESS_201, value={"teacher": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@teacher_routes.route("/<id>", methods=["GET"], strict_slashes=False)
def get_teacher_by_id(id):
    """
    Retrieve a teacher by their ID.

    This endpoint handles GET requests to fetch a teacher's details from the database using their unique ID.
    It utilizes the Teacher model to query the database and the TeacherSchema to serialize the data.

    Args:
        id (str): The unique identifier of the teacher to be retrieved.

    Returns:
        Response: A JSON response containing the teacher's details with a success status code 200.
                 In case of any exceptions, returns an error response with status code 500 and the error message.
    """

    try:
        fetched = Teacher.query.get(id)
        teacher_schema = TeacherSchema(many=False)
        teacher = teacher_schema.dump(fetched)
        print("teacher fetched by id successfully")
        return response_with(resp.SUCCESS_200, value={"teacher": teacher})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@teacher_routes.route("/", methods=["GET"], strict_slashes=False)
def get_all_teachers():
    """
    Retrieve all teachers from the database.

    This endpoint handles GET requests to fetch all teacher records from the database.
    It uses the `Teacher` model to query all teacher entries and serializes the data
    using the `TeacherSchema`. The serialized data is then returned in a JSON response
    with a success status code. If an error occurs during the process, a server error
    response is returned.

    Returns:
        Response: A JSON response containing a list of all teachers with a success status code.
                  In case of an error, a JSON response with a server error status code and the error message.
    """

    try:
        fetched = Teacher.query.all()
        teacher_schema = TeacherSchema(many=True)
        teachers = teacher_schema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"teachers": teachers})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@teacher_routes.route("/<id>", methods=["DELETE"], strict_slashes=False)
def delete_teacher(id):
    """
    Deletes a Teacher record from the database based on the provided ID.

    This endpoint handles DELETE requests to remove a Teacher from the database.
    It retrieves the Teacher by ID, deletes the record, commits the transaction,
    and returns a success response. If an error occurs during the process, it
    returns a server error response.

    Args:
        id (str): The ID of the Teacher to be deleted.

    Returns:
        Response: A JSON response indicating the result of the delete operation.
                  On success, it returns a 204 status code with the deleted Teacher's data.
                  On failure, it returns a 500 status code indicating a server error.
    """

    try:
        get_teacher = Teacher.query.get(id)
        db.session.delete(get_teacher)
        db.session.commit()

        print(f"Teacher with id {get_teacher} deleted successfully")
        teacher_schema = TeacherSchema()
        teacher = teacher_schema.dump(get_teacher)
        return response_with(resp.SUCCESS_200, value={"teacher": teacher})
    except Exception as e:
        return response_with(resp.SERVER_ERROR_500)


@teacher_routes.route("/<id>", methods=["PUT"], strict_slashes=False)
def update_teacher(id):
    """
    Updates an existing Teacher record in the database.

    This endpoint handles PUT requests to update a Teacher's information
    based on the provided ID. The function expects a JSON payload with the
    updated Teacher data. If the Teacher with the specified ID is found, the
    record is updated with the new data and the changes are committed to the
    database. If the Teacher is not found, a 404 error response is returned.
    In case of any other errors, a 422 error response is returned.

    Args:
        id (str): The ID of the Teacher to be updated.

    Returns:
        Response: A Flask response object with the updated Teacher data and
        appropriate HTTP status code.
    """

    try:
        data = request.get_json()
        get_teacher = Teacher.query.get(id)

        if not get_teacher:
            return response_with(resp.SERVER_ERROR_404, message="Teacher not found")

        if data:
            data["updated_at"] = str(datetime.utcnow())
            if data.get("class_id"):
                get_teacher.class_id = data["class_id"]

        teacher_schema = TeacherSchema()
        db.session.add(get_teacher)
        db.session.commit()
        teacher = teacher_schema.dump(get_teacher)
        print("Teacher updated successfully")
        return response_with(resp.SUCCESS_200, value={"teacher": teacher})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@teacher_routes.route("/<id>/students", methods=["GET"], strict_slashes=False)
def update_teacher_for_student(id):
    """Get all student related to the teacher"""

    try:
        get_teacher = Teacher.query.get(id)

        if not get_teacher:
            return response_with(resp.SERVER_ERROR_404, message="Teacher not found")

        students = get_teacher.get_all_students(get_teacher.class_id)
        if not students:
            raise Exception
        print("Student gotten successfuly")
        return response_with(resp.SUCCESS_200, value={"students": students})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422, value={"error": "no student"})
