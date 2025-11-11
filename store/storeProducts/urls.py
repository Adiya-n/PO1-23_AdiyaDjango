from django.urls import path
from storeProducts.views import index, products

app_name = 'storeProducts'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
]