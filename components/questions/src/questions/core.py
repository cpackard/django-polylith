# Standard Library
import datetime
from typing import TypedDict

# Third-Party Libraries
import pytz

# Django Libraries
from django.forms.models import model_to_dict

# Local Modules
from .models import Question as QuestionModel


class Question(TypedDict):
    question: str
    pub_date: datetime.datetime


def find_question(search: str) -> Question | None:
    question = (
        QuestionModel.objects.filter(question_text__contains=search).values().first()
    )
    question["pub_date"] = question["pub_date"].date()
    return question


def create_question(question: str) -> Question:
    new_q = QuestionModel.objects.create(
        question_text=question, pub_date=datetime.datetime.now(pytz.utc).date()
    )
    return model_to_dict(new_q)
