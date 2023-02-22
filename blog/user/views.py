from flask import Blueprint, render_template
from blog.articles.views import ARTICLES

user = Blueprint('user', __name__, static_folder='../static', url_prefix='/users')

USERS = {
    1: {'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday': '6 июня 1799 г.'},
    2: {'first_name': 'Михаил', 'last_name': 'Лермонтов', 'birthday': '15 октября 1814 г.'},
    3: {'first_name': 'Фёдор', 'last_name': 'Достоевский', 'birthday': '11 ноября 1821 г.'},
}

@user.route('/')
def user_list():
    return render_template(
        'user/list.html',
        users=USERS,
    )

@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        selected_user = USERS[pk]
    except KeyError:
        raise FileNotFoundError(f'User id {pk} not found')
    return render_template(
        'user/detail.html',
        selected_user=selected_user,
        articles=ARTICLES,
    )
