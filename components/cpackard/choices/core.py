# Standard Library
from typing import TypedDict

# Django Libraries
from django.apps import apps
from django.forms.models import model_to_dict


class Choice(TypedDict):
    question_id: int
    choice_text: str
    votes: int


def find_choices(question: int) -> list[Choice] | None:
    """Return all choices for the given `question`."""
    model = apps.get_model("choices", "Choice")
    return [choice for choice in model.objects.filter(question_id=question).values()]


def create_choice(question: int, choice: str) -> Choice:
    """Create a new `choice` associated with `question`."""
    model = apps.get_model("choices", "Choice")
    new_choice = model.objects.create(question_id=question, choice_text=choice, votes=0)
    return model_to_dict(new_choice)
