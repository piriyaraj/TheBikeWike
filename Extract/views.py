from email import message
import os
from django.shortcuts import render
from django.http import HttpResponse
from blog import models
from .modules import extracter,setmodels,urlexract
from django.contrib.auth.models import User
# Create your views here.
from django.core.files.uploadedfile import UploadedFile

# fd = open("tempImg/2022 AJS Tempest Roadster 125 bikespeci.webp", 'rb')
# newBikeImage = models.Bikeimage()
# newBikeImage.image = UploadedFile(fd)
# newBikeImage.alt = "image of  its show front, back, side view and show bike specifications"
# newBikeImage.save()
url = "https://bikez.com/motorcycles/aeon_cobra_400_supermoto_2022.php"


def extractpost(request):
    message = urlexract.updateBikePost()
    return HttpResponse(message, content_type='text/plain')


def updatemodel(request):
    urlexract.updateModel()
    return HttpResponse("Updated all models in database", content_type='text/plain')


def updateposturl(request):
    urlexract.updatePostUrl()
    return HttpResponse("Updated pending post urls in database", content_type='text/plain')


def test(request):
    urlexract.test()
    return HttpResponse("test posts updated", content_type='text/plain')
