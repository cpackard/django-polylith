from django.http import HttpRequest, JsonResponse


def index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({'result': 'test'})
