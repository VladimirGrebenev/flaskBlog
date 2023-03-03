import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg123456"
    WTF_CSRF_ENABLED = True


class DevConfig(BaseConfig):
    DEBUG = True
    if os.environ.get("SQLALCHEMY_DATABASE_URI"):
        # to set SQLALCHEMY_DATABASE_URI, use terminal: export SQLALCHEMY_DATABASE_URI=your_URI
        SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True
