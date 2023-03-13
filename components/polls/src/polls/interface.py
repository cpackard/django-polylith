# Standard Library
import datetime

# Third-Party Libraries
import pytz

# Local Modules
from .models import Choice, Question


def find_question(search: str) -> dict | None:
    """Returns the first question matching `search` or None."""
    return Question.objects.filter(question_text__contains=search).values().first()


def get_current_time() -> str:
    """Sample function to demo transitive dependencies."""
    return datetime.datetime.now(pytz.utc).strftime("%Y-%m-%d")
