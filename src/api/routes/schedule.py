from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.schedule import Schedule, ScheduleSchema
from api.utils.database import db

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

    fetched = Schedule.query.all()
    schedule_schema = ScheduleSchema(many=True)
    schedules = schedule_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"schdules": schedules})
