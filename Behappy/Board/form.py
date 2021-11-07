from django import forms
from django.db import models
from django.db.models.base import Model
from django.forms import fields, widgets

from.models import Board, Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['memberName','password']
        widgets = {'password':forms.PasswordInput}

class signupForm(forms.ModelForm):
    password_check = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={'class':'pw2'}))

    #field_order = ['memberName','password','password_check','name']
    class Meta:
        model = Member
        fields =  ['memberName', 'password', 'password_check', 'name']
        widgets = {
            'memberName' : forms.TextInput(attrs={'class': 'memberName'}),
            'password' : forms.PasswordInput(attrs={'class': 'pw1'}),
        }

class BoardWriteForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'user', 'content', 'member']
        widgets ={
            'title' : forms.TextInput(attrs={'class' : 'title'}),
            'user' : forms.TextInput(attrs={'class':'user'}),
            'content' : forms.TextInput(attrs={'class':'content'}),
            'member' : forms.HiddenInput(),
        }