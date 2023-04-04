# Standard Library
import datetime
from typing import TypedDict

# Third-Party Libraries
import pytz

# Django Libraries
from django.apps import apps
from django.forms.models import model_to_dict


class Question(TypedDict):
    question: str
    pub_date: datetime.datetime


def find_question(search: str) -> Question | None:
    """Return the first question matching `search`. Partial matches are valid."""
    model = apps.get_model("questions", "Question")
    question = model.objects.filter(question_text__contains=search).values().first()
    question["pub_date"] = question["pub_date"].date()
    return question


def create_question(question: str) -> Question:
    """Create a new `question`."""
    model = apps.get_model("questions", "Question")
    new_q = model.objects.create(question_text=question, pub_date=datetime.datetime.now(pytz.utc).date())
    return model_to_dict(new_q)
