from .models import Question, Choice


def find_question(search: str) -> dict | None:
    """Returns the first question matching `search` or None."""
    return Question.objects.filter(question_text__contains=search).values().first()
