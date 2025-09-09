"""
URL configuration for Newspaper_Site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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





from django.urls import path
from.views import create_post,rate_a_news,ditials_view,search_news,delete_a_post,update_a_post
urlpatterns = [
    path('create_post/',create_post, name='create_post'),
    path('rate_a_news/<int:pk>/',rate_a_news, name='rate_a_news'),
    path('ditials_view/<int:pk>/',ditials_view, name='ditials_view'),
    path('search_news/',search_news, name='search_news'),
    path('delete_a_post/<int:pk>/',delete_a_post, name='delete_a_post'),
    path('update_a_post/<int:pk>/',update_a_post, name='update_a_post'),
]