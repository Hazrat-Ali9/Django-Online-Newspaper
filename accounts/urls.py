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
from .views import singup,sign_in,see_my_profie,edit_my_profile,change_my_password,apply_as_editors,Logout,edotor_profile,all_of_a_editor

urlpatterns = [
     path('singup/', singup,name='singup'),
     path('sign_in/', sign_in,name='sign_in'),
     path('see_my_profie/', see_my_profie,name='see_my_profie'),
     path('edit_my_profile/', edit_my_profile,name='edit_my_profile'),
     path('changepassword/', change_my_password,name='changepassword'),
     path('apply_as_editors/', apply_as_editors,name='apply_as_editors'),
     path('Logout/', Logout,name='Logout'),
     path('edotor_profile/', edotor_profile,name='edotor_profile'),
     path('all_of_a_editor/', all_of_a_editor,name='all_of_a_editor'), 
]