# Django Libraries
from django.urls import include, path

# Local Modules
from . import views

urlpatterns = [
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path("api/questions/", views.questions_view, name="questions"),
    path("api/choices/", views.choices_view, name="choices"),
]
