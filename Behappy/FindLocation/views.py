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


def index(request):
    res = showBin()
    context = {'data' : '일반쓰레기','where' : res}
    kim = json.dumps(res)
    return render(request, 'findlocation/show.html', context)

def showDiffer(request):
    res = showBin()
    context = {'data' : '가로휴지통', 'where' : res}
    print(context)
    return render(request,'findlocation/seperate.html', context)
