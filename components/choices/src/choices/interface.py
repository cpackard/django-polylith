# Local Modules
from . import core


def find_choices(question: int) -> list[core.Choice] | None:
    """TODO: fill"""
    return core.find_choices(question)


def create_choice(question: int, choice: str) -> core.Choice:
    return core.create_choice(question, choice)
