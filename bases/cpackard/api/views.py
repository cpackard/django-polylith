# Django Libraries
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response

# Polylith Bricks
from cpackard.authentication import interface as auth
from cpackard.choices import interface as choices
from cpackard.choices_db import interface as choices_db
from cpackard.questions import interface as questions


class QuestionsPermission(permissions.BasePermission):
    """
    Global permission check for accessing questions.
    """

    def has_permission(self, request, view):
        return auth.email_check(request)


@api_view(["GET", "POST"])
@permission_classes([QuestionsPermission])
def questions_view(request: Request) -> Response:
    querydict = request.GET if request.method == "GET" else request.POST
    question = querydict.get("question", [None])[0]

    if question is None:
        return Response({"errors": ['You must include the "question" parameter.']}, status=400)

    if request.method == "GET":
        return Response({"result": questions.find_question(question)})
    elif request.method == "POST":
        return Response({"result": questions.create_question(question)}, status=201)

    return Response({"errors": ["Unsupported method."]}, status=405)


@api_view(["GET", "POST"])
@permission_classes([])
def choices_view(request: Request) -> Response:
    querydict = request.GET if request.method == "GET" else request.POST
    question: int = next(iter(querydict.get("question", [])), None)
    if question is None:
        return Response({"errors": ['You must include the "question" parameter.']}, status=400)

    if request.method == "GET":
        return Response({"result": choices.order_choices(choices_db.find_choices(question))})
    elif request.method == "POST":
        choice: str = next(iter(querydict.get("choice", [])), None)
        if choice is None:
            return Response({"errors": ['You must include the "choice" parameter.']}, status=400)

        return Response({"result": choices_db.create_choice(question, choice)}, status=201)

    return Response({"errors": ["Unsupported method."]}, status=405)
