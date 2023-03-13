# Django Libraries
from django.urls import path

# Local Modules
from . import views

urlpatterns = [
    path("api/questions/", views.search_question, name="search_question"),
    path("api/time/", views.current_time, name="current_time"),
]
