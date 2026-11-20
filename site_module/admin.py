from django.contrib import admin
from . import models
# Register your models here.
#

admin.site.register(models.SiteSettings)

admin.site.register(models.FooterBox)
admin.site.register(models.FooterBoxLink)


class BannerAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'url',
        'position',
        'is_active',
    ]
    list_editable = [
        
        'url',
        'position',
        'is_active',
    ]
admin.site.register(models.Banner,BannerAdmin)