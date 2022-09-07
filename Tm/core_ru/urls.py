from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('all_products_ru/', all_products, name='all_products_ru'),
    path('products_ru/<int:id>/', products, name='products_ru'),
    path('products_detail_ru/<int:id>/', products_detail, name='products_detail_ru'),
    path('contact_ru/', contact, name='contact_ru'),
    path('about_us_ru/', about_us, name='about_us_ru'),
]