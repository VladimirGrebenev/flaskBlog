import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg123456"
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cerulean'
    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class DevConfig(BaseConfig):
    DEBUG = True
    if os.environ.get("SQLALCHEMY_DATABASE_URI"):
        # to set SQLALCHEMY_DATABASE_URI, use terminal: export SQLALCHEMY_DATABASE_URI=your_URI
        # to run python wsgi.py in DevConfig, use terminal: export CONFIG_NAME=DevConfig
        SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True
