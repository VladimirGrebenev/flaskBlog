from flask import Blueprint, render_template
# from blog.articles.views import ARTICLES
from blog.models import User

user_app = Blueprint('user_app', __name__, static_folder='../static', url_prefix='/users')

# USERS = {
#     1: {'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday': '6 июня 1799 г.'},
#     2: {'first_name': 'Михаил', 'last_name': 'Лермонтов', 'birthday': '15 октября 1814 г.'},
#     3: {'first_name': 'Фёдор', 'last_name': 'Достоевский', 'birthday': '11 ноября 1821 г.'},
# }

@user_app.route('/')
def user_list():
    users = User.query.all()
    return render_template(
        'user/list.html',
        users=users,
    )

@user_app.route('/<int:user_id>/')
def user_profile(user_id: int):
    try:
        user = User.query.filter_by(id=user_id).one_or_none()
    except KeyError:
        raise FileNotFoundError(f'User id {user_id} not found')
    return render_template(
        'user/detail.html',
        user=user,
        # articles=ARTICLES,
    )
