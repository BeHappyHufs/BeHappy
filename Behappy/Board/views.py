from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *

from .form import BoardWriteForm, MemberForm, signupForm
from Board import form

# Create your views here.
def main(request):

    boardList = Board.objects.all()

    if request.method == 'POST':
        memberName = request.POST.get('memberName')
        password = request.POST.get('password')
        member = Member.objects.get(memberName=memberName,password=password)
        if member is not None:
            request.session['memberid'] = member.id
            return render(request, 'main.html', {'boardList' : boardList})

        else:
            return redirect('login')
    
    return render(request, 'main.html',{'boardList' : boardList})

def write(request):
    if request.method =='POST':
        form = BoardWriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    member_id = request.session['memberid']
    member = get_object_or_404(Member, pk=member_id)
    form = BoardWriteForm(initial={'member':member})
    return render(request, 'write.html', {'form':form, 'member':member})

def detail(request, boardid):
    board = get_object_or_404(Board,pk=boardid)
    
    try:
        session = request.session['memberid']
        context = {
            'board': board,
            'session': session,
        }
        return render(request,'detail.html',context)

    except KeyError:
        return redirect('main')



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

