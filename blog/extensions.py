from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from blog.models.user import User

login_manager = LoginManager()
db = SQLAlchemy()


__all__ = [
    'db',
    'User',
]

