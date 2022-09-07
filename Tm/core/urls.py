from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('all_products/', all_products, name='all_products'),
    path('products/<int:id>/', products, name='products'),
    path('products_detail/<int:id>/', products_detail, name='products_detail'),
    path('contact/', contact, name='contact'),
    path('about_us/', about_us, name='about_us'),
]