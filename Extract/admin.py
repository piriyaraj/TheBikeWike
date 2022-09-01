from django.contrib import admin

from Extract.models import  Model, Url

# Register your models here.


class ModelView(admin.ModelAdmin):
    list_display = ('name', 'noOfPost', 'status', 'modelLink')
    list_filter = ("name",)
    search_fields = ['name', 'modelLink']


class UrlView(admin.ModelAdmin):
    list_display = ('id','link', 'status', 'lastChecked', 'modelId', 'date')
    list_filter = ("postId",)
    search_fields = ['postId', 'status']

admin.site.register(Model, ModelView)
admin.site.register(Url, UrlView)
