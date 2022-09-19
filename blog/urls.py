from django.urls import path
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import blogSitemap
from .views import *

sitemaps={
    "blog":blogSitemap
}
urlpatterns = [
    path('', home, name='home'),
    path('blogs/', blogs, name='blogs'),
    path('brand/<str:slug>/', category_blogs, name='category_blogs'),
    path('page/<str:slug>/', page_details, name='page_details'),
    path('tag_blogs/<str:slug>/', tag_blogs, name='tag_blogs'),
    path('model/<str:slug>/', blog_details, name='blog_details'),
    path('add_reply/<int:blog_id>/<int:comment_id>/', add_reply, name='add_reply'),
    path('like_blog/<int:pk>/', like_blog, name='like_blog'),
    path('search_blogs/', search_blogs, name='search_blogs'),
    path('my_blogs/', my_blogs, name='my_blogs'),
    path('add_blog/', add_blog, name='add_blog'),
    path('update_blog/<str:slug>/', update_blog, name='update_blog'),
    path("sitemap.xml",sitemap,{'sitemaps':sitemaps})
]