# Local Modules
from . import core


def find_question(search: str) -> core.Question | None:
    return core.find_question(search)


def create_question(question: str) -> core.Question:
    return core.create_question(question)
