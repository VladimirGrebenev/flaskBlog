from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_login import current_user

from blog import models
from blog.models.database import db


# Customized admin interface
class CustomView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("auth_app.login"))


# Create protected admin index view
class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for("auth_app.login"))
        if not current_user.is_staff:
            error = 'this area is staff only'
            return redirect(url_for("index", error=error))
        return super(MyAdminIndexView, self).index()


# Create admin with custom props
admin_app = Admin(
    name="Blog Admin",
    index_view=MyAdminIndexView(),
    template_mode="bootstrap4",
)

# Add views
admin_app.add_view(CustomView(models.Article, db.session, category="Models"))


# Custom admin views
class TagAdminView(CustomView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    can_export = True
    export_types = ["csv", "xlsx"]
    create_modal = True
    edit_modal = True


admin_app.add_view(TagAdminView(models.Tag, db.session, category="Models"))


class UserAdminView(CustomView):
    column_exclude_list = ("_password",)
    column_searchable_list = ("first_name", "last_name", "username", "is_staff", "email")
    column_filters = ("first_name", "last_name", "username", "is_staff", "email")
    column_editable_list = ("first_name", "last_name", "is_staff")
    can_create = True
    can_edit = True
    can_delete = False


admin_app.add_view(UserAdminView(models.User, db.session, category="Models"))
