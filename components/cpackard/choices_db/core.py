# Django Libraries
from django.forms.models import model_to_dict

# Local Modules
from .models import Choice as ChoiceModel
from .types import Choice


def find_choices(question: int) -> list[Choice] | None:
    """Return all choices for the given `question`."""
    return [choice for choice in ChoiceModel.objects.filter(question_id=question).values()]


def create_choice(question: int, choice: str) -> Choice:
    """Create a new `choice` associated with `question`."""
    new_choice = ChoiceModel.objects.create(question_id=question, choice_text=choice, votes=0)
    return model_to_dict(new_choice)
