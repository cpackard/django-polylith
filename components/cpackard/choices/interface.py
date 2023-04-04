# Local Modules
from . import core


def find_choices(question: int) -> list[core.Choice] | None:
    """Return all choices for the given `question`."""
    return core.find_choices(question)


def create_choice(question: int, choice: str) -> core.Choice:
    """Create a new `choice` associated with `question`."""
    return core.create_choice(question, choice)
