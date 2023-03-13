from flask import Blueprint, render_template
from blog.models import User, Article
from flask_login import login_required, current_user

user_app = Blueprint('user_app', __name__, static_folder='../static', url_prefix='/users')


@user_app.route('/')
@login_required
def user_list():
    users = User.query.all()
    return render_template(
        'user/list.html',
        users=users,
    )


@user_app.route('/<int:user_id>/')
@login_required
def user_profile(user_id: int):
    try:
        user = User.query.filter_by(id=user_id).one_or_none()
        articles = Article.query.filter_by(author_id=user_id)
    except KeyError:
        raise FileNotFoundError(f'User id {user_id} not found')



    if current_user.is_staff is True:
        return render_template(
            'user/detail.html',
            user=user,
            articles=articles
        )
    else:
        error = 'this is staff area only'
        return render_template(
            'user/list.html',
            user=user,
            error=error,
        )
