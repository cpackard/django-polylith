from django.http import HttpRequest, JsonResponse

from polls import interface as polls


def search_question(request: HttpRequest) -> JsonResponse:
    search: str = next(iter(request.GET.get('search', [])), None)
    if search is None:
        return JsonResponse({'errors': ['You must include the "search" parameter.']}, status=400)
    return JsonResponse({'result': polls.find_question(search)})
