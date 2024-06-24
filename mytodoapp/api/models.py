from django.db import models
import string
import random

def generatecode():
    length=6
    while True:
        id='#'.join(random.choices(string.ascii_uppercase,k=length))
        if TodoLabel.objects.filter(code=id).count == 0:
            break
    return id

# Create your models here.
class TodoLabel(models.Model):
    # code=models.CharField(max_length=8,unique=True,default='')
    subject=models.CharField(max_length=40,default="Empty")
    description=models.TextField()