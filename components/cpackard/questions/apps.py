# Django Libraries
from django import apps as django_apps


class QuestionsConfig(django_apps.AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cpackard.questions"
