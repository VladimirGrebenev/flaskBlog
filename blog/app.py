from flask import Flask
from blog.user.views import user
from blog.articles.views import articles
from blog.models.database import db
from blog.auth.views import login_manager, auth_app


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprint(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.config["SECRET_KEY"] = "abcdefg123456"
    login_manager.init_app(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(articles)
    app.register_blueprint(auth_app, url_prefix="/auth")
