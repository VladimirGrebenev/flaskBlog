from flask import Flask
from blog.user.views import user
from blog.articles.views import articles

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprint(app)
    return app

def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(articles)
