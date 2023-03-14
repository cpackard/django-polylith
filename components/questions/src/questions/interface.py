# Local Modules
from . import core


def find_question(search: str) -> core.Question | None:
    """Return the first question matching `search`. Partial matches are valid."""
    return core.find_question(search)


def create_question(question: str) -> core.Question:
    """Create a new `question`."""
    return core.create_question(question)
