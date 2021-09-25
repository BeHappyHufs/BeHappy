from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode, unquote
from bs4 import BeautifulSoup
import requests
import json
from .api import showBin

@csrf_exempt
def showMap(request):
    if request.method =='GET':
        return render(request,'findlocation/map.html')

serviceKey = "	fZrdoxTt5AoPpbAJScuxo3IeZBzRVqrhnG%2FpP7J6uZfC05FIbniTRaZicjkRyJr8Tzs0RdKmFnQgRFUNPUyXDA%3D%3D"
serviceKeyDecoded = unquote

@csrf_exempt
def index(request):
    res = showBin()
    bin = res.get('일반 사각 쓰레기통')
    context = {'data': '서울특별시 구로구 구로동로 31', 'bin_kind' : bin}
    return render(request,'findlocation/show.html',context)
