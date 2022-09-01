from django.core.files.uploadedfile import UploadedFile
from django.shortcuts import get_object_or_404
from . import extracter, setmodels, urlexract
from django.contrib.auth.models import User
from pyexpat import model
import re
from unicodedata import name
import requests
from bs4 import BeautifulSoup
import os
from user_profile.models import User
from blog.models import Bikeimage, Blog, Biketable, Category
try:
    from Extract.models import Model, Url
except:
    from models import Model,Url
url = "https://bikez.com/brands/index.php"

def exractModelsLink(url):
    try:
        reqs = requests.get(url)
    except:
        print("check internet connection !")
        return []
    soup = BeautifulSoup(reqs.text, 'html.parser')
    table=soup.findAll('table',class_="zebra")[0]
    trs=table.findAll("tr")
    links=[]
    for i in trs[1:]:
        if(i.findAll("td")[1].text==""):
            # print("==>"+i.findAll("td")[0].text)
            continue
        atag=i.findAll("a")[0]

        link_m="https://bikez.com/"+atag.get_attribute_list("href")[0].split("../")[1]
        links.append(link_m)

    return links

def filemake(name):
    try:
        file=open(name,"r+")
    except:
        open(name,"w").close()
        file=open(name,"r+")
    return file

def expandUrlpost(url):
    post_links = []
    try:
        reqs = requests.get(url)
    except:
        print("Check Internet connection !")
        return []
    soup = BeautifulSoup(reqs.text, 'html.parser')
    table=soup.find_all('table')[2]
    tr=table.find_all('tr')
    # print(tr)
    for i in tr:
        if(tr.index(i)==0):
            continue
        tdTags = i.findAll('td')
        if(len(tdTags)>2 or len(tdTags[0].findAll('img'))==0):
            continue
        
        t=i.findAll('td')[1].findAll('a')
        for i in t:
            if(i.get_attribute_list('href')[0]==None):
                continue
            else:
                link="https://bikez.com"+i.get_attribute_list("href")[0].split("..")[1]
        post_links.append(link)
    return post_links

def exractpostlink(url):
    post_links=[]
    try:
        reqs = requests.get(url)
    except:
        print("Check Internet connection !")
        return []
    soup = BeautifulSoup(reqs.text, 'html.parser')
    table=soup.find_all('table')[2]
    tr=table.find_all('tr')
    # print(tr)
    for i in tr:
        if(tr.index(i)==0):
            continue
        expandTag = i.findAll('td')[0].findAll('a')
        if(len(expandTag)!=0):
            expandUrl=url+expandTag[0].get_attribute_list('href')[0]
            expandpostUrls = expandUrlpost(expandUrl)
            post_links=post_links+expandpostUrls
            continue
        
        t=i.findAll('td')[1].findAll('a')
        for i in t:
            if(i.get_attribute_list('href')[0]==None):
                continue
            else:
                link="https://bikez.com"+i.get_attribute_list("href")[0].split("..")[1]
        post_links.append(link)
    return post_links

def updateModelCount(modelId,count):
    modelId.noOfPost=count
    modelId.save()

def createCategory(name):
    newCatogery=Category()
    newCatogery.title=name
    newCatogery.slug=name
    newCatogery.save()

def createModel(noOfPost, modelLink,name):
    newModel=Model()
    newModel.noOfPost = noOfPost
    newModel.modelLink = modelLink
    newModel.name = name
    haveNewUpdate=True
    try:
        newModel.save()
    except:
        newModel=Model.objects.get(modelLink=modelLink)
        if(newModel.noOfPost != noOfPost):
            newModel.noOfPost=noOfPost
        else:
            haveNewUpdate=False
    return newModel, haveNewUpdate


def createUrl(link, modelId):
    newUrl=Url()
    newUrl.link=link
    newUrl.modelId=modelId
    # newUrl.postId = Bikepost.objects.first()
    isLinkAvailable=False
    try:
        newUrl.save()
    except Exception as e:
        print(e)
        isLinkAvailable=True

    return isLinkAvailable


def run():
    modelsLinks=exractModelsLink(url)
    for modelLink in modelsLinks:

        modelforfile = modelLink.split("models/")[1].split(".")[0]
        print("\n\n>>> "+modelforfile,end="")

        postlinks = exractpostlink(modelLink)
        newModel, haveNewPost = createModel(0, modelLink, modelforfile)

        if(not(haveNewPost)):
            print(" ||| No new post")
            continue
        print(" ||| NO of Post: ",len(postlinks))
        
        # links = fileModel.readlines()
        noOfPost=newModel.noOfPost
        for postlink in postlinks:
            createUrl(postlink,newModel)
            noOfPost+=1
            updateModelCount(newModel,noOfPost)
            # fileModel.write(postlink+"\n")
            print("======>>>"+postlink)


def updateModel():
    modelsLinks = exractModelsLink(url)
    for modelLink in modelsLinks[:1]:
        modelforfile = modelLink.split("models/")[1].split(".")[0]
        modelName = " ".join(modelforfile.split("_")).capitalize().split(" models")[0]
        # print(">>> "+modelName)
        createModel(0, modelLink, modelName)
        try:
            createCategory(modelName)
        except:
            pass
def updatePostUrl():
    modelObj=Model.objects.filter(status=0)
    # print(modelObj[:1])
    for i in modelObj[:1]:
        modelLink =i.modelLink
        modelforfile = modelLink.split("models/")[1].split(".")[0]
        # print("\n\n>>> "+modelforfile, end="")

        postlinks = exractpostlink(modelLink)

        if(i.noOfPost==len(postlinks)):
            i.status=1
            i.save()
            # print(" ||| No new post")
            continue
        # print(" ||| NO of Post: ", len(postlinks))

        # links = fileModel.readlines()
        noOfPost = i.noOfPost
        for postlink in postlinks:
            createUrl(postlink, i)
            noOfPost += 1
            updateModelCount(i, noOfPost)
            # fileModel.write(postlink+"\n")
            # print("======>>>"+postlink)
        if(noOfPost == len(postlinks)):
            i.status = 1
            i.save()


def updateBikePost():  # update every post content , images and data table
    urlsObjs=Url.objects.filter(status=0)
    # print(len(urlsObjs))
    for i in urlsObjs[:1]:
        title, key, value, images, contant,category = extracter.getdata(i.link)
        print(category)

        
        
        # create post
        # user = User.objects.get(id=1)
        cateId = Category.objects.get(title=category).id
        category = get_object_or_404(Category, pk=cateId)
        user = get_object_or_404(User, pk=1)

        newBikePost = Blog()
        newBikePost.title = title
        newBikePost.slug = title#.split(" |")[0].replace(" ", "_").lower().replace(".","_")
        newBikePost.description = contant
        newBikePost.category = category
        newBikePost.user = user
        newBikePost.banner = UploadedFile(open(images[0], 'rb'))
        # newBikePost.status = 1

        # newBikePost.author = user
        try:
            newBikePost.save()
        except:
            bikepost=Blog.objects.get(title=title)
            i.status=1
            i.postId = bikepost
            i.save()
            return "This post already available"
        
        # create table object
        newBikeTable = Biketable()
        newBikeTable = setmodels.table(newBikeTable, key, value)
        newBikeTable.idofblog=newBikePost
        newBikeTable.save()
        

        # create image object
        for j in images:
            fd = open(j, 'rb')
            newBikeImage = Bikeimage()
            newBikeImage.image = UploadedFile(fd)
            newBikeImage.postId = newBikePost
            newBikeImage.alt = "image of " + \
                title.split(" |")[
                    0]+" its show front, back, side view and show bike specifications"
            newBikeImage.save()
            # os.remove(i)
        i.status=1
        i.postId = newBikePost
        i.save()
        return "done"
    return "Post extract successfully"

#postlinks_n="https://bikez.com/year/2020-motorcycle-models.php"
#linkss=exractpostlink(postlinks_n)
def test():
    updateModel()
    updatePostUrl()
    updateBikePost()

if __name__ == "__main__":
    # run()

    # postLinks = exractpostlink("https://bikez.com/models/ajs_models.php")
    # print(len(postLinks))

    # expandpostUrls = expandUrlpost(
    #     "https://bikez.com/models/access_models.php?expser=2784#explist")
    # print(expandpostUrls)
    print(updateModel(url))
