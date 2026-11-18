from django.shortcuts import render
from .models import Product, ProductCategory,Brand

from django.db.models import Avg
from django.views.generic import ListView, DeleteView
from . import models
from django.db.models import Count
# Create your views here.


class ProductListView(ListView):
    model = models.Product
    template_name = 'product_module/product_list.html'
    context_object_name ='products_list'
    
    paginate_by =2

    def get_queryset(self):
        category = self.kwargs.get('category')
        brand = self.kwargs.get('brand')
        queryset = super().get_queryset()
        if category:
            queryset = queryset.filter(category__url_title = category)
        if brand:
            queryset = queryset.filter(brand__title = brand)
        queryset = queryset  # TODO
        return queryset




def product_list(request):
    products_list = Product.objects.all().order_by('-price')
    context = {
        'products_list': products_list,
        'count':Product.objects.count(),
        'AVG':Product.objects.aggregate(Avg('price'))
        }
    return render(request, 'product_module/product_list.html',context=context)



class ProductDetailView(DeleteView):
    template_name = 'product_module/product_detail.html'
    model = Product
    context_object_name = 'product'

def product_detail(request, slug ):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
        }
    return render(request, 'product_module/product_detail.html',context=context)


def product_categories_component(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'product_module/category_component.html', context )




def product_brand_component(request):
    context = {
        'brands': Brand.objects.all().annotate(product_count = Count('products'))
    }
    return render(request, 'product_module/brands_component.html', context )