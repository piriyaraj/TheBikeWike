"""
scrapping table from link
creat :29/12/2020
update:30/12/2020
"""
from doctest import testmod
from PIL import ImageFilter
from unicodedata import category
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import re
import requests
from bs4 import BeautifulSoup
import os
try:
    from . import constant, articalWriter
except:
    import constant,articalWriter
# import articalWriter
testMode=True

def downloadImg(soup):
    try:
        os.mkdir("tempImg")
    except:
        pass
    imgList=[]
    table = soup.find_all('table')[1]
    a_tags = table.find_all('a')
    a_tag=a_tags[0]['href']
    # print("a url  : ",a_tag)
    img_tag=a_tags[0].find_all("img")
    imgList.append(img_tag[0]["src"])

    while(a_tag.find("pictno")>0):
        a_tagList=a_tag.split("=")
        # print(a_tagList[1])
        a_tag=a_tagList[0]+"="+str(int(a_tagList[1])+1)

        reqs = requests.get(a_tag)
        soup1 = BeautifulSoup(reqs.text, 'html.parser')
        table = soup1.find_all('table')[1]
        
        a_tags = table.find_all('a')
        a_tag1=a_tags[0]['href']
        img_tag1 = a_tags[0].find_all("img")
        if(img_tag1[0]['src'].find("pictures")<0):
            break
        img_url = "https://bikez.com/"+img_tag1[0]["src"].split("../")[1]
        imgList.append(img_url)
        # print("a url  : ",a_tag)

# https: // bikez.com/pictures/ajs/2022/58346_0_1_2_tempest % 20roadster % 20125_Image % 20credits % 20-%20AJS.jpg
    imgTitleList=[]
    for i in range(len(imgList)):
        img_title = "./tempImg/"+soup.title.text.split('specifications')[0].split(" |")[0]+"TheBikeWiki "+str(i)+'.webp'
        img_url = imgList[i]
        res = requests.get(img_url)
        file = open(img_title, 'wb')
        for chunk in res.iter_content(10000):
            file.write(chunk)
        file.close()
        imgTitleList.append(img_title)
    return imgTitleList

def imgtext(bikeName, keys,values):
    divtag = soup.findAll("div",class_="inside-grid-column")
    text1 = ""

    try:
        text1 += "Model              :"+bikeName+"\n\n"
    except:
            pass
    try:
        text1 += "Year                :"+values[keys.index("Year")]+"\n\n"
    except:
            pass
    try:
        text1 += "Category         :"+values[keys.index("Category")]+"\n\n"
    except:
            pass
    try:
        text1 += "Price                :"+values[keys.index("Price as new")].split(".")[0]+"\n\n"
    except:
            pass
    try:
        text1 += "Power              :"+values[keys.index("Power")]+"\n\n"
    except:
            pass
    try:
        text1 += "Top speed       :"+values[keys.index("Top speed")]+"\n\n"
    except:
            pass
    try:
        text1 += "Fuel capacity  :"+values[keys.index("Fuel capacity")]+"\n\n"
    except:
            pass
    try:
        text1 += "Reserve fuel   :"+values[keys.index("Reserve fuel capacity")]+"\n\n"
    except:
            pass
    try:
        val = values[keys.index("Color options")].replace(",","\n                         -")
        text1 += "Color options  :"+val+"\n\n"
    except:
            pass

    # print(text1)
    text1 += "                                                TheBikeWiki"
    return text1

def addLogo(text1, logo,image):
    if(testMode):
        print("logo adding start")
    image1 = Image.open(image) # open the images
    image1 = image1.resize((1200, 900))  # 1280*1920
    draw = ImageDraw.Draw(image1)
    font = ImageFont.truetype("arial.ttf", 30)
    #x, y = (width - 510, height-100)
    image1_size = image1.size

    # add middle text
    # text = "TheBikeWiki"
    # w, h = font.getsize(text)
    # x, y = int((image1_size[0]-w)/2), int((image1_size[1]-h)/2)
    # x1,y1 = int((5.5*image1_size[0]/10)),int((image1_size[1]/10))
    # draw.rectangle((x, y, x + w, y + h), fill='black')
    # draw.text((x, y), text, fill=(209, 239, 8), font=font)


    image2 = Image.open(logo)  # open logo
    image1_size = image1.size        # get image size
    # image2 = image2.resize((int(image1_size[0]/3), int(image1_size[1]/4)))# resize the logo as 1/9 image size
    image2_size = image2.size        # get the resized logo sizes
    # new_image = Image.new('RGB',(image1_size[0], 2*image1_size[1]), (250,250,250))  #create new image size as old image size
    new_image = Image.new('RGB', (image1_size[0], 2*image1_size[1]), (255,255,255))  #create new image size as old image size
    new_image.paste(image1, (0,0))    # insert image into new image we created
    # new_image.paste(image2, ((image1_size[0]-image2_size[0],image1_size[1]-image2_size[1]))) # insert resized logo into the new image
    # print(text1)
    x1 = 780


    y1 = 680
    x2 = 1170
    y2 = 900

    # Create rectangle mask
    mask = Image.new('L', new_image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle([(x1, y1), (x2, y2)], fill=255)
    # mask.save('mask.png')

    # Blur image
    blurred = new_image.filter(ImageFilter.GaussianBlur(15))

    # add copyright
    w, h = image2.size
    x, y = int((image1_size[0]-w)/2), int((image1_size[1]-h)/2)
    new_image.paste(image2,(x,y),image2)


    # Paste blurred region and save result
    new_image.paste(blurred, mask=mask)
    draw = ImageDraw.Draw(new_image)
    draw.rectangle(
        (0, int(new_image.size[1]/2), new_image.size[0], new_image.size[1]), fill='#101820FF')
    font = ImageFont.truetype("arial.ttf", 40)
    draw.text((20, int(new_image.size[1]/2)+10),
              text1, fill="#FEE715FF", font=font)
    new_image.save(image , "webp")         # save new image
    if(testMode):
        print("logo added")
    return image


def getdata(url):
    global soup

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    for i in soup.find_all('table'):
        if(i.text.find("General information") !=-1 or i.text.find("General moped information")!=-1 or i.text.find("Other specifications")!=-1):
            table = i
            break
    #print(table)
    title = soup.title.text
    tags = title.split()[1]+","+title.split()[0]
    year = title.split()[0]
    bike_name = title.replace(" specifications and pictures","").replace(title.split()[0]+" ","")
    if(title.find("|") >0):
        # print("loop",title)
        tags = title.split()[0]+","+title.split("|")[1].replace(" ","")
        title = title.split()[0]+" "+title.split()[0]+" "+title
        # print("loop",title)
        bike_name = title

    title = title.replace(" specifications and pictures","").replace(title.split()[0]+" ","")+" | Price, Photos, Millage, Speed, Colours etc."

    if(title.find(tags.split(",")[0]) <0):
        title = tags.split(",")[0]+" "+title
    # print("loop",title)

    title = title.split(" |")[0] +" "+year+" | Price, Photos, Mileage, Speed, Colors, etc"
    descri = "Find NAME price, speed, mileage, images, specifications, news, videos, Colours and variants information at TheBikeWiki. More Details.".replace("NAME",bike_name)
    #print(title+"\n"+tags+"\n"+descri)

    ind = str(table).index("Further")
    contant = str(table)[:ind-len("""<tr><th  colspan="2" style="background-color: #cccccc; text-align: center;"><a name="FURTHER"></a>""")]
    for i in table.findAll('a'):
        contant = contant.replace(str(i),i.text)
    contant = contant.replace("#CCCCCC","#99c9ff")
    contant = contant.replace("width:100%","color: black; width: 100%;")
    contant = contant.replace("</tr><tr><th","""</tr></tbody></table><br/><table class="Grid" style="color: black; width: 100%;"><tbody><tr><th""")

    contant = contant.replace("<table","<table align=\"center\"")
    contant = contant.replace("25%","40%")
    contant = contant.replace("90%","100%")
    contant = contant.replace("100%;\"><tr><th","100%;\"><tbody><tr><th")
    contant = contant.replace(">General"," id=\"1\"><strong>"+bike_name+" General ")
    contant = contant.replace(">Engine and transmission"," id=\"2\"><strong>"+bike_name+" Engine and transmission ")
    contant = contant.replace(">Chassis"," id=\"3\"><strong>"+bike_name+" Chassis")
    contant = contant.replace(">Physical"," id=\"4\"><strong>"+bike_name+" Physical")
    contant = contant.replace(">Other"," id=\"5\"><strong>"+bike_name+" Other ")
    contant = constant.table_contant+contant+"""</tr></tbody></table>"""
    contant = contant.replace("</tr><tr><th","""</tr></tbody></table><br/><table align="center" class="Grid" style="color: black; width: 100%;"><tbody><tr><th""")

    #remove rating
    rate_ind_start = contant.index("<tr><td style=\"vertical-align:top;width:40%;\"><b>Rating")
    rate_ind_end  = contant[rate_ind_start:].index("</tr>")
    #print(rate_ind_start,rate_ind_end)
    remove_rating = (contant[rate_ind_start:rate_ind_end+rate_ind_start+5])
    contant = contant.replace(remove_rating,"")
    contant = contant.replace("moped","")

    contant = contant.replace("bike_name",title.split(" |")[0])


    contant = contant.replace("</th>","</strong></th>")

    artical,keys,values = articalWriter.artical(soup)
    contant += artical

    text1 = imgtext(title.split(" |")[0],keys,values)
    downloadedImg=[]
    try:
        for i in downloadImg(soup):
            downloadedImg.append(addLogo(text1, "./thebikewiki.png", i))
    except Exception as e:
        if(testMode):
            print(e)
        downloadedImg.append("./TheBikeWiki_thumbnail.png")
    # pimage = addLogo(text1, "./LOGO.png", downloadImg(soup))
    category=soup.find("h1").find("a").text
    # , tags,descri,contant,pimage
    return title.split(" |")[0], keys, values, downloadedImg, contant, category

# url="https://bikez.com/motorcycles/access_ams_320_supercross_2016.php"
# url1="https://bikez.com/motorcycles/arctic_cat_alterra_570_eps_se_2021.php"
# # url2="https://bikez.com/motorcycles/bmw_r_ninet_2021.php"
#
# title,tags,descri,contant,pimage=getdata(url1)
# pyperclip.copy(contant)
# print(contant)
# print(tags,"\n"+title+"\n\n")
# print()
# title,tags,descri,contant,pimage=getdata(url1)
# print(tags,"\n"+title+"\n\n")


# reqs = requests.get(url)
# soup = BeautifulSoup(reqs.text, 'html.parser')
# print(addLogo(text1,"./LOGO.png",downloadImg(soup)))
# reqs = requests.get(url1)
# soup = BeautifulSoup(reqs.text, 'html.parser')
# print(downloadImg(soup))

# urlbest="https://bikez.com/motorcycles/bmw_r_nine_t_2015.php"
# reqs = requests.get(url2)
# soup = BeautifulSoup(reqs.text, 'html.parser')
# title=soup.title.text
# title=title.replace(" specifications and pictures","").replace(title.split()[0]+" ","")+" | Price, Photos, Millage, Speed, Colours etc."
# artical,keys,values=articalWriter.artical(soup)
# text1=imgtext(title.split(" |")[0],keys,values)
# pimage=addLogo(text1,"./LOGO.png",downloadImg(soup))

# 1280*1920

# print(addLogo("./LOGO.png",downloadImg(soup)))
if __name__=="__main__":
    url = "https://bikez.com/motorcycles/aeon_cobra_400_supermoto_2022.php"
    url = "https://bikez.com/motorcycles/ajs_125_eco_commuter_2010.php"
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    # addLogo("aeon cobra 400", "./thebikewiki.png", downloadImg(soup)[0])
    # print(downloadImg(soup))
    getdata(url)
