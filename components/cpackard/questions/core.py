# Standard Library
import datetime

# Third-Party Libraries
import pytz

# Django Libraries
from django.forms.models import model_to_dict

# Local Modules
from .models import Question as QuestionModel
from .types import Question


def find_question(search: str) -> Question | None:
    """Return the first question matching `search`. Partial matches are valid."""
    question = QuestionModel.objects.filter(question_text__contains=search).values().first()
    question["pub_date"] = question["pub_date"].date()
    return question


def create_question(question: str) -> Question:
    """Create a new `question`."""
    new_q = QuestionModel.objects.create(question_text=question, pub_date=datetime.datetime.now(pytz.utc).date())
    return model_to_dict(new_q)
