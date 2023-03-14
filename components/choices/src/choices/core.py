# Standard Library
from typing import TypedDict

# Django Libraries
from django.forms.models import model_to_dict

# Local Modules
from .models import Choice as ChoiceModel


class Choice(TypedDict):
    question_id: int
    choice_text: str
    votes: int


def find_choices(question: int) -> list[Choice] | None:
    return [
        choice for choice in ChoiceModel.objects.filter(question_id=question).values()
    ]


def create_choice(question: int, choice: str) -> Choice:
    new_choice = ChoiceModel.objects.create(
        question_id=question, choice_text=choice, votes=0
    )
    return model_to_dict(new_choice)
