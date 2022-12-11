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
    path("", views.main),



    path("chiefs/", views.chiefs),
    path("add_chief/", views.add_chief),
    path("edit_chief/<int:id>/", views.edit_chief),
    path("delete_chief/<int:id>/", views.delete_chief),

    path("posts/", views.posts),
    path("add_post/", views.add_post),
    path("edit_post/<int:id>/", views.edit_post),
    path("delete_post/<int:id>/", views.delete_post),

    path("guards/", views.guards),
    path("add_guard/", views.add_guard),
    path("edit_guard/<int:id>/", views.edit_guard),
    path("delete_guard/<int:id>/", views.delete_guard),

    path("on_duties/", views.on_duties),
    path("add_on_duty/", views.add_on_duty),
    path("edit_on_duty/<int:id>/", views.edit_on_duty),
    path("delete_on_duty/<int:id>/", views.delete_on_duty),
]
