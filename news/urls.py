"""rtk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.views.generic import ListView, DetailView
from news.models import News
from news.views import NewsListView, AuthorBookList

urlpatterns = [
    path('', NewsListView.as_view(), name='news'),
      #path('<int:pk>', DetailView.as_view(model=News, template_name='news/single.html'))
    path('<int:pk>', DetailView.as_view(model=News, template_name='news/single.html')),
     path('find/<author_name>', AuthorBookList.as_view()),
    path('ex/ex', views.ex, name='ex'),

    path('create', views.create, name='create')

]
