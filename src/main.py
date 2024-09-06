import logging
import os
import sys
from flask import Flask, jsonify
from flask_cors import CORS
from api.config.config import DevelopmentConfig, ProductionConfig, TestingConfig
from api.utils.database import db
from api.utils.responses import response_with
import api.utils.responses as resp


# Initialize the Flask app
app = Flask(__name__)
CORS(app)


# Import routes
from api.routes.admin import admin_routes
from api.routes.parents import parent_routes
from api.routes.students import student_routes
from api.routes.schedule import schedule_route
from api.routes.teachers import teacher_routes
from api.routes.classes import class_routes
from api.routes.subjects import subject_routes
from api.routes.class_subject import class_subject_r
from api.routes.student_subject import st_subject

# Determine environment and load corresponding config
if os.getenv("WORK_ENV") == "PROD":
    app_config = ProductionConfig
elif os.getenv("WORK_ENV") == "TEST":
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)

# Initialize database
db.init_app(app)

with app.app_context():
    db.create_all()


# Register Blueprints

app.register_blueprint(teacher_routes, url_prefix="/api/teachers")
app.register_blueprint(subject_routes, url_prefix="/api/subjects")
app.register_blueprint(class_subject_r, url_prefix="/api/class_sub")
app.register_blueprint(class_routes, url_prefix="/api/classes")
app.register_blueprint(schedule_route, url_prefix="/api/schedules")
app.register_blueprint(student_routes, url_prefix="/api/students")
app.register_blueprint(st_subject, url_prefix="/api/student_subject")
app.register_blueprint(admin_routes, url_prefix="/api/admins")
app.register_blueprint(parent_routes, url_prefix="/api/parents")


# START GLOBAL HTTP CONFIGS
@app.after_request
def add_header(response):
    return response


# Error Handlers
@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)


@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)


@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)


# logging Configuration
logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s",
    level=logging.DEBUG,
)

# Main entry point
if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False)
