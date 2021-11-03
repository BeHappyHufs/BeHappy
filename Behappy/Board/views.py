from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *

from .form import MemberForm, signupForm
from Board import form

# Create your views here.
def main(request):
    if request.method == 'POST':
        memberName = request.POST.get('memberName')
        password = request.POST.get('password')
        member = Member.objects.get(memberName=memberName,password=password)
        if member is not None:
            request.session['memberid'] = member.id
            return render(request, 'main.html', {'memberId' : member.name})
        else:
            return redirect('login')
    boards = {'boards': Board.objects.all()}
    return render(request, 'main.html', boards)

def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('main'))
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
    return render(request, 'main.html', boards)



#로그인
def login(request):
    form = MemberForm()
    return render(request,'login.html',{'form': form})


def signUp(request):
    if request.method =='POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = signupForm()
    return render(request,'signup.html',{'form': form})

