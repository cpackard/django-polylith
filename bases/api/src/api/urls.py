from django.urls import path

from . import views

urlpatterns = [
    path('api/questions/', views.search_question, name='search_question'),
]
