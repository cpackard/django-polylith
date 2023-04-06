# Third-Party Libraries
from celery import Celery
from celery.utils.log import get_task_logger

# Polylith Bricks
from cpackard.choices import interface as choices

# NOTE: command to run is:
# poetry run celery -A cpackard.processing_worker.core worker --loglevel=INFO
app = Celery("processing_worker", broker="sqla+sqlite:///celery.sqlite", backend="db+sqlite:///celery.sqlite")

logger = get_task_logger(__name__)


@app.task
def top_question(unordered_choices: list[choices.Choice]) -> None:
    sorted_choices = choices.order_choices(unordered_choices)
    if not sorted_choices:
        return

    top_choice = sorted_choices[0]
    logger.info(
        "Top choice for question %s is %s with %i votes",
        top_choice["question_id"],
        top_choice["choice_text"],
        top_choice["votes"],
    )
