# Django Libraries
from django.urls import include, path

# Local Modules
from . import views

urlpatterns = [
    path("api/questions/", views.questions_view, name="questions"),
    path("api/choices/", views.choices_view, name="choices"),
]
