# Standard Library
from typing import TypedDict


class Choice(TypedDict):
    question_id: int
    choice_text: str
    votes: int
