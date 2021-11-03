from django.db import models

# Create your models here.
class Board(models.Model):
    author = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Member(models.Model):
    memberName = models.CharField(max_length=10)
    password = models.CharField(max_length=60)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)