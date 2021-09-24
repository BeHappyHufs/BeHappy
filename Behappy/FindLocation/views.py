from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def showMap(request):
    if request.method =='GET':
        return render(request,'findlocation/map.html')