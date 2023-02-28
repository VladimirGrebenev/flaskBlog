from sqlalchemy import Column, Integer, String, Boolean
from flask_login import UserMixin

from blog.models.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255))
    is_staff = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<User #{self.id} {self.username!r}>'

    def __init__(self, username, email, password, is_staff):
        self.username = username
        self.email = email
        self.password = password
        self.is_staff = is_staff
