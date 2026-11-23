from django.shortcuts import render

# Create your views here.
from rest_framework.request import Request
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from product_module.models import Product

from .serializers import ProductSerializer

@api_view(['GET','POST'])
def productAPI(request: Request):
    if request.method == 'GET':
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products,many=True)
        
        return Response(serializer.data , status= status.HTTP_200_OK)
    
    elif request.method == 'POST':
        request_data = request.data
        serializer = ProductSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)
    return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def productAPIById(request: Request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)