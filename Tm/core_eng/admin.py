from django.contrib import admin
from .models import *



class SliderAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_editable = ['is_active',]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sale', 'category', 'new', ]
    list_editable = ['sale', 'new']



admin.site.register(Slider, SliderAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ContactUs)
admin.site.register(Galleria)
admin.site.register(About_us)
admin.site.register(Contacts)