# Polylith Bricks
from cpackard.questions import core

# Local Modules
from .types import Question


def find_question(search: str) -> Question | None:
    """Return the first question matching `search`. Partial matches are valid."""
    return core.find_question(search)


def create_question(question: str) -> Question:
    """Create a new `question`."""
    return core.create_question(question)
