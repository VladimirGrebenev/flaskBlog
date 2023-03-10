from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from sqlalchemy.orm import joinedload

from blog.models.database import db
from blog.models import Author, Article, Tag, User
from blog.forms.article import CreateArticleForm

articles_app = Blueprint('articles_app', __name__, url_prefix='/articles')


@articles_app.route("/", endpoint="list")
@login_required
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)


@articles_app.route("/tag/<int:tag_id>/", endpoint="list_by_tag")
@login_required
def articles_list_by_tag(tag_id):
    tag = Tag.query.filter_by(id=tag_id).options(joinedload(Tag.articles)).one_or_none()
    if tag is None:
        raise NotFound
    return render_template("articles/articles_by_tag.html", tag=tag)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_detals(article_id):
    article = Article.query.filter_by(id=article_id).options(
        joinedload(Article.tags)  # подгружаем связанные теги!
    ).one_or_none()
    if article is None:
        raise NotFound
    return render_template("articles/detail.html", article=article)


@articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    # добавляем доступные теги в форму
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if request.method == "POST" and form.validate_on_submit():  # при создании статьи
        article = Article(title=form.title.data.strip(), body=form.body.data)
        if form.tags.data:  # если в форму были переданы теги (были выбраны)
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
        for tag in selected_tags:
            article.tags.append(tag)  # добавляем выбранные теги к статье
        if current_user.author:
            # use existing author if present
            article.author = current_user.author
        else:
            # otherwise create author record
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = current_user.author
        try:
            db.session.add(article)
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles_app.details", article_id=article.id))
    return render_template("articles/create.html", form=form, error=error)
