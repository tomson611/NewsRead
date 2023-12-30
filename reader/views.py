from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

import requests

from newsread.local_settings import API_KEY


def read_view(request):
    url = f'https://newsapi.org/v2/top-headlines?country=pl&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()  
    api_data = data['articles']
    return render(request, 'reader/reader.html', {'api_data': api_data})   

