# Django Libraries
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Polylith Bricks
from cpackard import choices, questions, surveys


@csrf_exempt
def surveys_view(request: HttpRequest) -> JsonResponse:
    querydict = request.GET if request.method == "GET" else request.POST
    satisfaction = next(iter(querydict.get("satisfaction", [])), None)

    if satisfaction is None:
        return JsonResponse({"errors": ['You must include the "satisfaction" parameter.']}, status=400)

    if request.method == "GET":
        return JsonResponse({"result": surveys.find_positive_surveys(satisfaction)})

    elif request.method == "POST":
        response_text = querydict["response_text"]

        if response_text is None:
            return JsonResponse({"errors": ['You must include the "response_text" parameter.']}, status=400)

        return JsonResponse({"result": surveys.create_survey(satisfaction, response_text)}, status=201)

    return JsonResponse({"errors": ["Unsupported method."]}, status=405)


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
