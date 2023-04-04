# Third-Party Libraries
from cpackard.choices import interface as choices
from cpackard.questions import interface as questions

# Django Libraries
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def questions_view(request: HttpRequest) -> JsonResponse:
    querydict = request.GET if request.method == "GET" else request.POST
    question: str = next(iter(querydict.get("question", [])), None)
    if question is None:
        return JsonResponse({"errors": ['You must include the "question" parameter.']}, status=400)

    if request.method == "GET":
        return JsonResponse({"result": questions.find_question(question)})
    elif request.method == "POST":
        return JsonResponse({"result": questions.create_question(question)}, status=201)

    return JsonResponse({"errors": ["Unsupported method."]}, status=405)


@csrf_exempt
def choices_view(request: HttpRequest) -> JsonResponse:
    querydict = request.GET if request.method == "GET" else request.POST
    question: int = next(iter(querydict.get("question", [])), None)
    if question is None:
        return JsonResponse({"errors": ['You must include the "question" parameter.']}, status=400)

    if request.method == "GET":
        return JsonResponse({"result": choices.find_choices(question)})
    elif request.method == "POST":
        choice: str = next(iter(querydict.get("choice", [])), None)
        if choice is None:
            return JsonResponse({"errors": ['You must include the "choice" parameter.']}, status=400)

        return JsonResponse({"result": choices.create_choice(question, choice)}, status=201)

    return JsonResponse({"errors": ["Unsupported method."]}, status=405)
