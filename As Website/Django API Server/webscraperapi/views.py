from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # Allow request without csrf_token set
from rest_framework.decorators import api_view

# Import my_worker from .utilities
from .utilities import web_scraper_worker
from .utilities import word_query_worker

@csrf_exempt
@api_view('POST')
def web_scraper(request, url):
    """
    Do something with 
    """
    if request.method == 'POST':
        # Call the utilities script here
        result = web_scraper_worker(url)
        return JsonResponse({'result': result})

@csrf_exempt
@api_view('POST')
def word_query(request, word):
    """
    Do something with 
    """
    if request.method == 'POST':
        # Call the utilities script here
        result = word_query_worker(word)
        return JsonResponse({'result': result})