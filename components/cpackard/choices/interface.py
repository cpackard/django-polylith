# Polylith Bricks
from cpackard.choices import core

# Local Modules
from .types import Choice


def find_choices(question: int) -> list[Choice] | None:
    """Return all choices for the given `question`."""
    return core.find_choices(question)


def create_choice(question: int, choice: str) -> Choice:
    """Create a new `choice` associated with `question`."""
    return core.create_choice(question, choice)
