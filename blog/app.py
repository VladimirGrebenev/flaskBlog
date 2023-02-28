from flask import Flask
from blog.extensions import db, login_manager
from blog.models import User
from blog import commands


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')

    register_extensions(app)
    register_blueprint(app)
    register_commands(app)

    return app

def register_extensions(app):
    db.init_app(app)
    login_manager.login_view = 'auth_app.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get


def register_blueprint(app: Flask):
    from blog.user.views import user_app
    from blog.articles.views import articles_app
    from blog.auth.views import auth_app

    app.register_blueprint(user_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(auth_app, url_prefix="/auth")


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db, 'init-db')
    app.cli.add_command(commands.create_init_users, 'create-users')

