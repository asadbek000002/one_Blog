import django.contrib.sitemaps.views
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from BlogApp.sitemaps import PostSitemaps

sitemaps = {
    'posts': PostSitemaps
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BlogApp.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
