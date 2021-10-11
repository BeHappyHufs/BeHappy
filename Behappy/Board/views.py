from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import *

# Create your views here.
def index(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'list.html', boards)

def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'post.html')

def detail(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail.html', {'board': board})

@csrf_exempt
def update(request,boardid):
    if request.method =='POST':
        board = Board.objects.get(pk=boardid)
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title is not None and board is not None:
            board.title = title
            board.content = content
            board.save()
            #return redirect('detail', boardid=boardid)
            return render(request, 'detail.html', {'board': board})
        else:
            #return redirect('detail', boardid=boardid)
            return render(request, 'detail.html', {'board': board})


def delete(request, boardid):
    board = Board.objects.get(id=boardid)
    board.delete()
    boards = {'boards': Board.objects.all()}
    return render(request, 'list.html', boards)