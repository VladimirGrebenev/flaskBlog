from flask import Blueprint, render_template
from flask_login import login_required
from blog.models import Author, Article

authors_app = Blueprint("authors_app", __name__)


@authors_app.route("/", endpoint="list")
@login_required
def authors_list():
    authors = Author.query.all()
    return render_template("authors/list.html", authors=authors)


@authors_app.route('/<int:author_id>/')
@login_required
def author_profile(author_id: int):
    try:
        author = Author.query.filter_by(id=author_id).one_or_none()
        articles = Article.query.filter_by(author_id=author_id)
    except KeyError:
        raise FileNotFoundError(f'Author id {author_id} not found')

    return render_template(
        'authors/detail.html',
        author=author,
        articles=articles
    )