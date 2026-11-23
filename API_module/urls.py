from django.urls import path
from .views import *

urlpatterns = [
    path('product', productAPI),
    path('product/<int:id>', productAPIById),
]
