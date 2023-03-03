from flask import Flask, render_template
from blog.models.database import db
from blog.user.views import user_app
from blog.articles.views import articles_app
from blog.auth.views import auth_app
from werkzeug.security import generate_password_hash
from blog.auth.views import login_manager
from flask_migrate import Migrate
import os

app = Flask(__name__)

# to run python wsgi.py in DevConfig, use terminal: export CONFIG_NAME=DevConfig
cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)
login_manager.init_app(app)

app.register_blueprint(user_app)
app.register_blueprint(articles_app)
app.register_blueprint(auth_app, url_prefix="/auth")


@app.route("/")
def index():
    return render_template("index.html")


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models.user import User

    admin = User(username="admin", is_staff=True, email='admin@mail.ru', password=generate_password_hash('admin123'))
    james = User(username="james", is_staff=False, email='james@mail.ru', password=generate_password_hash('james123'))

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)
