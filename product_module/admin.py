from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category', 'is_active']
    list_display = ['title', 'price','short_description','is_active', 'is_delete','image','brand']
    list_editable = ['price','is_active']

class ProductVisitAdmin(admin.ModelAdmin):
    list_display =['product','ip','user']

admin.site.register(Product,ProductAdmin )
admin.site.register(ProductCategory )
admin.site.register(ProductTags )
admin.site.register(Brand)
admin.site.register(ProductVisit,ProductVisitAdmin)
admin.site.register(ProductGallery)