from django.contrib import admin

# Register your models here.
from . import models

class OrdersAdmin(admin.ModelAdmin):
    list_display =[
        'user',
        'is_paid',
        'payment_date'
    ]

admin.site.register(models.Orders ,OrdersAdmin)



class Order_detailsAdmin(admin.ModelAdmin):
    list_display =[
        'product',
        'order',
        'count',
        'final_price',
    ]

admin.site.register(models.Order_details ,Order_detailsAdmin)