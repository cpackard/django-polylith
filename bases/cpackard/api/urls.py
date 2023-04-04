# Django Libraries
from django.urls import path

# Local Modules
from . import views

urlpatterns = [
    path("api/questions/", views.questions_view, name="questions"),
    path("api/choices/", views.choices_view, name="choices"),
    path("api/surveys/", views.surveys_view, name="surveys"),
]
