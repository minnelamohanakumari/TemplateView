"""project45 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('CBV_html/',CBV_html.as_view(),name='CBV_html'),
    path('CBV_html/',TemplateView.as_view(template_name='CBV_html.html'),name='CBV_html'),
    path('cbv_context/',cbv_context.as_view(),name='cbv_context'),
    path('cbv_forms/',cbv_forms.as_view(),name='cbv_forms'),
]