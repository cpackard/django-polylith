# Standard Library
from operator import itemgetter

# Local Modules
from .types import Choice


def order_choices(choices: list[Choice]) -> list[Choice]:
    """Order choices by votes, grouped by question."""
    return sorted(choices, key=itemgetter("question_id", "votes"), reverse=True)
