from django.http import HttpRequest, JsonResponse, HttpResponse
from WebScraper import WebScraper
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        if 'url' in json_data:
            print('POST with url: ' + json_data['url'])
            url = json_data['url']
            scraper = WebScraper()
            scraper.scrape_url(url)
            scraper.save()
            return HttpResponse(status = 200)
        elif 'word' in json_data:
            print('POST with word: ' + json_data['word'])
            word = json_data['word']
            scraper = WebScraper()
            results = scraper.query_results_file(word)
            print(results)
            return JsonResponse(results, safe=False, status = 200)
        else:
            print('POST with no data')
            return HttpResponse(status = 400)
    else:
        print("Default")
        return JsonResponse({'message': 'Hello, world!'})