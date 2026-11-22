from django.urls import path
from .views import *

urlpatterns = [
    path('add_product_to_order/',add_product_to_order ,name="add_product_to_order"),
    path("cart/", CartView.as_view(), name="shopping-cart"),
    path("remove_item_from_cart/", RemoveItemFromCart, name = "remove_item_from_cart"), 
    path("change_count_item_from_cart/", ChangeCountItemInCart, name = "change_count_item_from_cart"), 
    path("CartComponent/", ChangeCountItemInCart, name = "change_count_item_from_cart"), 
]
