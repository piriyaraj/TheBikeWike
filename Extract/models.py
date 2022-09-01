from asyncio.windows_events import NULL
from pyexpat import model
from tkinter import CASCADE
from xml.etree.ElementInclude import default_loader
from django.db import models

from blog.models import Blog

STATUS = (
    (0, "Pending"),
    (1, "Extracted")
)

# Create your models here.
class Model(models.Model):
    name=models.CharField(max_length=100)
    noOfPost=models.IntegerField(default=0)
    modelLink=models.URLField(unique=True,default=NULL)
    status = models.IntegerField(choices=STATUS, default=0)


class Url(models.Model):
    link=models.URLField(unique=True,default=NULL)
    status=models.IntegerField(choices=STATUS,default=0)
    modelId=models.ForeignKey(Model,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    lastChecked = models.DateTimeField(auto_now_add=True)
    postId = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True,blank=True)
