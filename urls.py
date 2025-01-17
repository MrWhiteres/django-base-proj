"""aaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import djoser

import settings.base
from apps.movies.views import MovieList
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include(('django.contrib.auth.urls', 'auth'), namespace='auth')),
    path('authentication/', include('apps.authentication.urls', namespace='authentication')),
    path('movies/', include('apps.movies.urls', namespace='movies')),
    path('select2/', include('django_select2.urls')),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('', MovieList.as_view()),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.base.STATIC_URL, document_root=settings.base.STATIC_ROOT)
