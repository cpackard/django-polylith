# Standard Library
from typing import TypedDict

# Django Libraries
from django.apps import apps
from django.forms.models import model_to_dict


class Survey(TypedDict):
    satisfaction: int
    response_text: str


def find_positive_surveys(satisfaction: int) -> list[Survey]:
    """Return all survey responses whose satisfaction is higher than the requested level."""
    model = apps.get_model("surveys", "Survey")
    return [survey for survey in model.objects.filter(satisfaction__gte=satisfaction).values()]


def create_survey(satisfaction: int, response_text: str) -> Survey:
    """Create a new survey response."""
    model = apps.get_model("surveys", "Survey")
    new_survey = model.objects.create(satisfaction=satisfaction, response_text=response_text)
    return model_to_dict(new_survey)
