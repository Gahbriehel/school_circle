import os
from urllib.parse import quote_plus

passwd = quote_plus(os.getenv("SCH_CIR_DB_PASS"))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = quote_plus(os.getenv("SCH_CIR_JWT_KEY", "fd"))


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL = (
        f"mysql+pymysql://root:{passwd}@localhost:3306/school_circle"
    )
    # SECRET_KEY = quote_plus(os.getenv("SCH_CIR_JWT_KEY"))


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://root:{passwd}@localhost:3306/school_circle"
    )
    SQLALCHEMY_ECHO = False
    # SECRET_KEY = quote_plus(os.getenv("SCH_CIR_JWT_KEY"))


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://root:{passwd}@localhost:3306/school_circle"
    )
    SQLALCHEMY_ECHO = False
    # SECRET_KEY = quote_plus(os.getenv("SCH_CIR_JWT_KEY"))
