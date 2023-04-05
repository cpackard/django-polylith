# Django Libraries
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

# Polylith Bricks
from cpackard import choices, questions, surveys, users


@api_view(["GET", "POST"])
def surveys_view(request: Request) -> Response:
    querydict = request.GET if request.method == "GET" else request.POST
    satisfaction = next(iter(querydict.get("satisfaction", [])), None)

    if satisfaction is None:
        return Response({"errors": ['You must include the "satisfaction" parameter.']}, status=400)

    if request.method == "GET":
        return Response({"result": surveys.find_positive_surveys(satisfaction)})

    elif request.method == "POST":
        response_text = querydict["response_text"]

        if response_text is None:
            return Response({"errors": ['You must include the "response_text" parameter.']}, status=400)

        return Response({"result": surveys.create_survey(satisfaction, response_text)}, status=201)

    return Response({"errors": ["Unsupported method."]}, status=405)


@api_view(["GET", "POST"])
def questions_view(request: Request) -> Response:
    querydict = request.GET if request.method == "GET" else request.POST
    # question = querydict.get("question", [None])[0]
    # question: str = next(iter(querydict.get("question", [])), None)
    question: str = querydict["question"]
    # username: str = querydict["username"]

    # ok = users.email_check(username)
    # if not ok:
    #     return Response({"errors": ["You do not have permissions to use this resource."]}, status=403)

    if question is None:
        return Response({"errors": ['You must include the "question" parameter.']}, status=400)

    if request.method == "GET":
        return Response({"result": questions.find_question(question)})
    elif request.method == "POST":
        return Response({"result": questions.create_question(question)}, status=201)

    return Response({"errors": ["Unsupported method."]}, status=405)


@api_view(["GET", "POST"])
def choices_view(request: Request) -> Response:
    querydict = request.GET if request.method == "GET" else request.POST
    question: int = next(iter(querydict.get("question", [])), None)
    if question is None:
        return Response({"errors": ['You must include the "question" parameter.']}, status=400)

    if request.method == "GET":
        return Response({"result": choices.find_choices(question)})
    elif request.method == "POST":
        choice: str = next(iter(querydict.get("choice", [])), None)
        if choice is None:
            return Response({"errors": ['You must include the "choice" parameter.']}, status=400)

        return Response({"result": choices.create_choice(question, choice)}, status=201)

    return Response({"errors": ["Unsupported method."]}, status=405)
