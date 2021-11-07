from django.db import models

# Create your models here.
class Member(models.Model):
    memberName = models.CharField(max_length=10)
    password = models.CharField(max_length=60)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=255)
    user = models.CharField(max_length=20)
    member = models.ForeignKey(Member , on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
