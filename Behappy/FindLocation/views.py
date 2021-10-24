from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode, unquote
from bs4 import BeautifulSoup
from django.http.response import HttpResponse
import requests
import json

from urllib3.response import HTTPResponse
from .api import showBin
import xml.etree.ElementTree as elemTree

@csrf_exempt
def showMap(request):
    if request.method =='GET':
        return render(request,'findlocation/map.html')
@csrf_exempt
def whereBin(request):
    res = showBin()
    context = json.dumps(res)
    print(context)
    return render(request, 'findlocation/bin.html', {"where": context})

@csrf_exempt
def index(request):
    res = showBin()
    context = json.dumps(res,ensure_ascii=False)
    return render(request, 'findlocation/show.html', {"where" : context})

@csrf_exempt
def showDiffer(request):
    res = showBin()
    context = json.dumps(res, ensure_ascii=False)
    return render(request,'findlocation/seperate.html', {"where": context})

@csrf_exempt
def search(request):
    res = showBin()
    context = json.dumps(res, ensure_ascii=False)
    return render(request,'findlocation/search.html', {"where": context})
