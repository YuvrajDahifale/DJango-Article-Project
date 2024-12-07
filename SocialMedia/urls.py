"""
URL configuration for SocialMedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from SocialMediaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ArticleList,name='article_list'),
    path('article_used<id>/<slug>', views.ArticleDetails,name='article_used'),
    path('create_article', views.CreateArticles,name='create_article'),
    path('userlogin', views.UserLogin,name='userlogin'),
    path('logout_view', views.LogOut,name='logout_view'),
    path('registration/', views.UserRegistration, name='registration'),
    path('logo/', views.LOGO, name='logo'),
    path('like_article', views.Like_Article, name='like_article')
    ]
