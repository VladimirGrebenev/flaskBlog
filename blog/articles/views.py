from flask import Blueprint, render_template
from flask_login import login_required

articles_app = Blueprint('articles_app', __name__, static_folder='../static', url_prefix='/articles')

ARTICLES = {
    1: {
        'title': 'Title 1',
        'author': {
            'id': 1,
            'name': 'Пушкин',
        },
        'text': 'article body text 1'
    },
    2: {
        'title': 'Title 2',
        'author': {
            'id': 2,
            'name': 'Лермонтов',
        },
        'text': 'article body text 2'
    },
    3: {
        'title': 'Title 3',
        'author': {
            'id': 1,
            'name': 'Достоевский',
        },
        'text': 'article body text 3'
    }
}


@articles_app.route('/')
@login_required
def articles_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )


@articles_app.route('/<int:pk>')
@login_required
def get_article(pk: int):
    try:
        article = ARTICLES[pk]
    except KeyError:
        raise FileNotFoundError(f'Article id {pk} not found')
    return render_template(
        'articles/detail.html',
        article=article,
    )
