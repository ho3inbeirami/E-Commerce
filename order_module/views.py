from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponseRedirect,HttpResponse
from django.urls import reverse
from product_module.models import Product
from order_module.models import Orders, Order_details
from django.views import View
from django.template.loader import render_to_string
from .models import *
# Create your views here.
from django.http import HttpRequest
def add_product_to_order(request: HttpRequest):
    product_id = request.GET.get('productId')
    count = int(request.GET.get('count'))
    if count <=0:
        return JsonResponse(
            {
                'status':'Invalid_count',
                'title':"Alert",
                'text': "Invalid product count",
                'icon': "error"
                }
            )
    
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id,is_active =True, is_delete = False).first()
        if product is not None:
            order , _ = Orders.objects.get_or_create(user = request.user,is_paid=False)
            order_detail= Order_details.objects.filter(order_id=order.id,product_id=product_id).first()
            if order_detail is not None :
                order_detail.count += count
                order_detail.save()
            else:
                order_detail= Order_details.objects.create(order_id=order.id,product_id=product_id, count = count)
            return JsonResponse(
                {
                    'status':'success',
                    'title':"Alert",
                    'text': "product add to cart",
                    'icon': "success"
                    }
            )
        else:
            return JsonResponse(
                {
                    'status':'Fail',
                    'title':"Alert",
                    'text': "product not fount",
                    'icon': "error"
                    }
            )
    else:
        return JsonResponse(
            {
                'status':'auth_error',
                'title':"Alert",
                'text': "Login required",
                'icon': "error"
                }
        )
    



def CartComponent(request):
    user = request.user.id
    order, _  = Orders.objects.get_or_create(user_id=user,is_paid =False)
    
    details = Order_details.objects.filter(order_id=order.id)
    total = 0
    
    for pro in details.all():
        total +=pro.product.price * pro.count
    
    context = {
        'details':details,
        'total': total
    }
    return render(request, 'order_module/cart_component.html', context)



class CartView(View):
    def get(self, request):
        user = request.user.id
        order, _  = Orders.objects.get_or_create(user_id=user,is_paid =False)
        
        details = Order_details.objects.filter(order_id=order.id)
        total = 0
        
        for pro in details.all():
            total +=pro.product.price * pro.count
        
        context = {
            'details':details,
            'total': total
        }
            
        
        return render(request,'order_module/cart.html',context)



def RemoveItemFromCart(request: HttpRequest):
    user = request.user
    product_id = request.GET.get("productId")
    order = Orders.objects.filter(user=user,is_paid=False).first()
    detail = Order_details.objects.filter(order =order, product_id = product_id)
    detail.delete()
    
    details = Order_details.objects.filter(order_id=order.id)
    total = 0
    
    for pro in details.all():
        total +=pro.product.price * pro.count
        
        
    context = {
            'details':details,
            'total': total
        }
    
    return JsonResponse({
        'status':'success',
        'data': render_to_string('order_module/cart_component.html',context,request)
    }
    )
    


def ChangeCountItemInCart(request: HttpRequest):
    user = request.user
    product_id = request.GET.get("productId")
    change = request.GET.get("increase")
    order = Orders.objects.filter(user=user,is_paid=False).first()
    detail = Order_details.objects.filter(order =order, product_id = product_id).first()
    if change=="1":
        detail.count = detail.count + 1
        detail.save()
    else:
        detail.count = detail.count - 1
        detail.save()
        if detail.count ==0:
            detail.delete()
            
    details = Order_details.objects.filter(order_id=order.id)
    total = 0
    
    for pro in details.all():
        total +=pro.product.price * pro.count
        
        
    context = {
            'details':details,
            'total': total
        }
    
    return JsonResponse({
        'status':'success',
        'data': render_to_string('order_module/cart_component.html',context,request)
    }
    )