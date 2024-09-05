from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.schedule import Schedule
from api.utils.database import db
from api.models.schemas import ScheduleSchema

schedule_route = Blueprint("schedule_routes", __name__)


@schedule_route.route("/", methods=["POST"], strict_slashes=False)
def create_schedule():
    try:
        data = request.get_json()
        schedule_schema = ScheduleSchema()
        schedule = schedule_schema.load(data)
        result = schedule_schema.dump(schedule.create())
        return response_with(resp.SUCCESS_201, value={"schedule": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@schedule_route.route("/", methods=["GET"], strict_slashes=False)
def get_all_schedule():

    try:
        fetched = Schedule.query.all()
        schedule_schema = ScheduleSchema(many=True)
        schedules = schedule_schema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"schdules": schedules})
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))


@schedule_route.route("/<id>", methods=["PUT"], strict_slashes=False)
def update_schedule(id):

    try:
        get_schedule = Schedule.query.get(id)

        if not get_schedule:
            return response_with(resp.SERVER_ERROR_404, message="Schedule not found")

        data = request.get_json()

        print("Right here")
        if data:
            if data.get("class_id"):
                get_schedule.class_id = data["class_id"]
            if data.get("subject_id"):
                get_schedule.subject_id = data["subject_id"]
                print("just check 0")
            if data.get("teacher_id"):
                get_schedule.teacher_id = data["teacher_id"]
                print("just check after")

        db.session.commit()

        Schedule_schema = ScheduleSchema()
        schedule = Schedule_schema.dump(get_schedule)
        return response_with(resp.SUCCESS_204, value={"schedule": schedule})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_FILED_NAME_SENT_422)


@schedule_route.route("/<id>", methods=["DELETE"], strict_slashes=False)
def delete_schedule(id):
    try:
        schedule = Schedule.query.get(id)

        if not schedule:
            return response_with(resp.SERVER_ERROR_404, message="Schedule not found")
        db.session.delete(schedule)
        db.session.commit()
        return response_with(resp.SUCCESS_204, message="Schedule deleted successfully")
    except Exception as e:
        print(e)
        return response_with(resp.SERVER_ERROR_500, message=str(e))
