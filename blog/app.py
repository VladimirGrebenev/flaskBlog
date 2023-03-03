from flask import Flask, render_template
from blog.models.database import db
from blog.user.views import user_app
from blog.articles.views import articles_app
from blog.auth.views import auth_app
from blog.auth.views import login_manager
from flask_migrate import Migrate
from blog.security import flask_bcrypt
import os

app = Flask(__name__)

# Config
# to run python wsgi.py in DevConfig, use terminal: export CONFIG_NAME=DevConfig
cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")

# Init
flask_bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)
login_manager.init_app(app)

# register_blueprints
app.register_blueprint(user_app)
app.register_blueprint(articles_app)
app.register_blueprint(auth_app, url_prefix="/auth")


# Route
@app.route("/")
def index():
    return render_template("index.html")


# Commands
@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    ➜ flask create-admin
    > created admin: <User #1 'admin'>
    """
    from blog.models import User
    admin = User(username="admin", is_staff=True, email='admin_email@email.ru')
    # to set admin password, use terminal: export ADMIN_PASSWORD=your_password
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"
    db.session.add(admin)
    db.session.commit()
    print("created admin:", admin)
