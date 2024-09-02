import logging
import os
import sys
from flask import Flask, jsonify
from api.config.config import DevelopmentConfig, ProductionConfig, TestingConfig
from api.utils.database import db
from api.utils.responses import response_with
import api.utils.responses as resp
from api.routes.admin import admin_routes
from api.routes.teachers import teacher_routes


app = Flask(__name__)

if os.getenv("WORK_ENV") == "PROD":
    app_config = ProductionConfig
elif os.getenv("WORK_ENV") == "TEST":
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)

# jwt = JWTManager(app)
db.init_app(app)

with app.app_context():
    db.create_all()


# TODO blueprint route register to be done here
app.register_blueprint(admin_routes, url_prefix="/api/admins")
app.register_blueprint(teacher_routes, url_prefix="/api/teachers")


# START GLOBAL HTTP CONFIGS
@app.after_request
def add_header(response):
    return response


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


# app.init_app(app)
# with app.app_context():
#     db.create_all()
logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s",
    level=logging.DEBUG,
)

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False)
