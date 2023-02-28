import os
from dotenv import load_dotenv
from blog.enums import EnvType

load_dotenv()

ENV = os.getenv('FLASK_ENV', default=EnvType.production)
DEBUG = ENV == EnvType.development
# FLASK_DEBUG = os.getenv('FLASK_DEBUG', default=EnvType.production)

SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') #sqlite:////tmp/blog.db
SQLALCHEMY_TRACK_MODIFICATIONS = False
