from django.contrib import admin
from django.urls import path, include
from api.views import hello, product_list, category_list, product_detail, category_detail, all_products_from_category
# product_detail
urlpatterns = [
    path('hello/', hello),
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_detail),
    path('categories/<int:category_id>/products/', all_products_from_category)
]