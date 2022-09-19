from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Blog
from blog.models import Blog


class blogSitemap(Sitemap):
    def items(self):
        return Blog.objects.all()

        