from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product_list_page' ),
    path('products/category/<category>', views.ProductListView.as_view(), name='product_list_page_filter' ),
    path('products/brand/<brand>', views.ProductListView.as_view(), name='product_list_page_brand_filter' ),
    path('products/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail_page' )
]
