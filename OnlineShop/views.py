from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from OnlineShop.models import Item
import ast 


def home_page(request):
    return render(request, "home.html")
    

def item_list(request):
    mydata = Item.objects.all()
    template = loader.get_template('item.html')
    context = {
        'myitems': mydata,
    }
    return HttpResponse(template.render(context, request))

def get_item_drinks(request):
    mydata = Item.objects.filter(category__exact='Drinks')
    template = loader.get_template('drinks.html')
    context = {
        'mydrinks': mydata,
    }
    return HttpResponse(template.render(context, request))

def get_item_technique(request):
    mydata = Item.objects.filter(category__exact='Technique')
    template = loader.get_template('technique.html')
    context = {
        'mytechnique': mydata,
    }
    return HttpResponse(template.render(context, request))
    

def get_item_food(request):
    mydata = Item.objects.filter(category__exact='Food')
    template = loader.get_template('food.html')
    context = {
        'myfood': mydata,
    }
    return HttpResponse(template.render(context, request))
    


def show_user_account(request):
    return render(request, 'user.html')

def user_signup(request):
    return render(request, "signup.html")

def user_login(request):
    return render(request, "login.html")


def user_logout(request):
    pass

def user_update(request):
    pass

def delete_user(reguest):
    pass


def create_item(request):
    return render(request, "create_item.html")

def update_item(request):
    pass

def find_item_by_id(request):
    pass

def delete_item(request):
    pass

def create_order(request):
    return render(request, "create_order.html")

def find_order_by_id(request):
    pass

def delete_order(request):
    pass
