"""hell_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<nome>/<int:idade>', views.hello),
    path('soma/<int:numero1>/<int:numero2>/', views.soma),
    path('subtracao/<int:numero1>/<int:numero2>/', views.subtracao),
    path('multiplicacao/<int:numero1>/<int:numero2>/', views.multplicacao),
    path('divisao/<int:numero1>/<int:numero2>/', views.divisao),
]