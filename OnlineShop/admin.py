from django.contrib import admin
from OnlineShop.models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

admin.site.register(User, PostAdmin)


class AdminItem(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'price', 'status', 'description')
    list_display_links = ('item_name',)
    list_editable = ('category', 'price', 'status', 'description')
    list_filter = ('status', 'category')

admin.site.register(Item, AdminItem)

class AdminOrder(admin.ModelAdmin):
    list_display = ('time_order', 'user', 'item')
    list_filter = ('time_order', 'user', 'item')



admin.site.register(Order, AdminOrder)
