from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'blog', 'search']
#todo ajouter url 'private' et 'game' (et 'article' ?)
#! 'blog/views.blog' à modifier view function or pattern name
    
    def location(self, item):
        return reverse(item)