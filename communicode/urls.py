"""communicode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from communicode.accounts.views import custom_registration_view

urlpatterns = [
    url(r'^$', 'communicode.views.dashboard_view', name='dashboard'),
    url(r'^project/(?P<project_id>\d+)/', 'communicode.views.project_code_view', name='project_code'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/register/$', custom_registration_view, name='register'),
]
urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
