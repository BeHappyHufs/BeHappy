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




def index(request):
    res = showBin()
    print(res)
    context = {'data' : '일반쓰레기','where' : res}
    print(context)
    return render(request, 'findlocation/show.html', context)
    #return HTTPResponse(res)
    # bin = res.get('일반 사각 쓰레기통')
    # context = {'data': '서울특별시 구로구 구로동로 31', 'bin_kind' : bin}
    # return render(request,'findlocation/show.html',context)
