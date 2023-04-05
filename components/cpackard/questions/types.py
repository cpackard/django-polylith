# Standard Library
import datetime
from typing import TypedDict


class Question(TypedDict):
    question: str
    pub_date: datetime.datetime
