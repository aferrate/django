from django.shortcuts import render        
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
        
def supermarket_get_offers(request):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"

    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    URL = "https://realpython.github.io/fake-jobs/"
    page = session.get(URL)

    return HttpResponse(page.text)

def index(request):
    return HttpResponse('<p><a href="/admin">admin</a></p><p><a href="/supermarket/getoffers/dia">supermarket dia get offers</a></p>') 