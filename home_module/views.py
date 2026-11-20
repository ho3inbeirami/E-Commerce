from django.shortcuts import render
from django.views .generic import TemplateView
from site_module.models import SiteSettings,FooterBox,FooterBoxLink
from . import models
from utils.grouped_list import group_list

from product_module.models import Product

# def index_page(request):
#     return render(request,'home_module/index.html')

class HomeView(TemplateView):
    template_name = 'home_module/index.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        sliders = models.Slider.objects.filter(is_active=True)
        populated_products = Product.objects.filter(is_active=True)[:12]
        context['populated_products'] = group_list(populated_products,4)
        context['sliders'] = sliders
        return context

def header_component(request):
    site = SiteSettings.objects.filter(is_main_setting = True).first()
    return render(request, 'shared/header_component.html', {'site':site})


def footer_component(request):
    site = SiteSettings.objects.filter(is_main_setting = True).first()
    footerbox = FooterBox.objects.all()
    footerboxlink = FooterBoxLink.objects.all()
    
    context = {
        'site':site,
        'footerbox':footerbox,
        'footerboxlink':footerboxlink,
        }
    
    return render(request, 'shared/footer_component.html',context )


class AboutView(TemplateView):
    template_name = 'home_module/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site =SiteSettings.objects.filter(is_main_setting= True).first()
        context["site"] =  site
        return context
    
