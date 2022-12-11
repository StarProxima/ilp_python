"""metanit URL Configuration

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
from django.urls import path, include
from hello import views

urlpatterns = [
    path("", views.glavn),

    path("brend/",views.index),
    path("brend/create/", views.create),
    path("stock/",views.index2),
    path("stock/create2/", views.create2),

    path("product/",views.index3),
    path("product/create/", views.create3),
    path("product/edit/<int:id>/", views.edit),
    path("product/open/<int:id>/", views.allinf),





]
