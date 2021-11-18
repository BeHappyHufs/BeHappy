from django.db import models

# Create your models here.
class Member(models.Model):
    ID = models.CharField(max_length=10,primary_key=True)
    password = models.CharField(max_length=60)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=255)
    member = models.ForeignKey(Member , on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
