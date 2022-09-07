from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('all_products_eng/', all_products, name='all_products_eng'),
    path('products_eng/<int:id>/', products, name='products_eng'),
    path('products_detail_eng/<int:id>/', products_detail, name='products_detail_eng'),
    path('contact_eng/', contact, name='contact_eng'),
    path('about_us_eng/', about_us, name='about_us_eng'),
]