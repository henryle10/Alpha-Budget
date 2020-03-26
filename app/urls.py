from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home),
    path("dash", views.dash),
    path("register_page", views.register_page),
    path("sign_in", views.sign_in),
    path("register", views.reg),
    path("login", views.log),
    path("logout", views.logout),
    path("dash", views.dash),
    path("edit_page", views.edit_page),
    path("edit_info", views.edit_info),
    path("about_page", views.about_page),
    path("calendar_page", views.calendar_page),
    path("splurge/<int:id>", views.splurge),
    path("delete/<int:id>", views.delete),
    path("manage_page", views.manage_page),
    path("expenses", views.expenses),
]
