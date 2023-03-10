"""shop URL Configuration

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
from OnlineShop.views import *

urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('shop/', item_list),
    path('user/', show_user_account),
    path('user/signup', user_signup),
    path('user/login', user_login),
    path('item/create', create_item),
    path('order/create', create_order),
    path('item/drinks', get_item_drinks),
    path('item/food', get_item_food),
    path('item/technique', get_item_technique)




]
