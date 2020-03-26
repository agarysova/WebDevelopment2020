from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
import json
from api.models import Product, Category
from django.http import Http404


# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello, world!</h1>')


def product_list(request):
    # select * from api_product
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    # select * from api_product where id= product_id
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': 'product does not exist'})

    return JsonResponse(product.to_json())


def category_list(request):
    # select * from api_categories
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    # select * from api_categories where id= category_id
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 'category does not exist'})

    return JsonResponse(category.to_json())


def all_products_from_category(request, category_id):
    # SELECT * FROM api_product WHERE id = category_id
    products = Product.objects.filter(category_id=category_id)

    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)
