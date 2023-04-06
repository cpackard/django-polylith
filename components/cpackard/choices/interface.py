# Polylith Bricks
from cpackard.choices import core

# Local Modules
from .types import Choice


def order_choices(choices: list[Choice]) -> list[Choice]:
    """Order choices by votes, grouped by question."""
    return core.order_choices(choices)
