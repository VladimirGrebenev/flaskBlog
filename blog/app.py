from flask import Flask
from blog.models.database import db
from blog.auth.views import login_manager


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')
    register_blueprint(app)
    db.init_app(app)
    login_manager.init_app(app)
    return app


def register_blueprint(app: Flask):
    from blog.user.views import user_app
    from blog.articles.views import articles_app
    from blog.auth.views import auth_app

    app.register_blueprint(user_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(auth_app, url_prefix="/auth")