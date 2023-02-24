from blog.app import create_app
from blog.models.database import db
from werkzeug.security import generate_password_hash
from flask import render_template

app = create_app()


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
    from blog.models import User

    admin = User(username="admin", is_staff=True, email='admin@mail.ru', password=generate_password_hash('admin123'))
    james = User(username="james", is_staff=False, email='james@mail.ru', password=generate_password_hash('james123'))
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)
