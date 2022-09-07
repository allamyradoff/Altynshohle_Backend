from django.shortcuts import render, redirect
from .models import *
from .forms import *



def main(request):
    slider = Slider.objects.filter(is_active=True)
    category = Category.objects.all()
    sale_product = Product.objects.filter(sale=True)[:6]
    new_product = Product.objects.filter(new=True)[:6]
    contacts = Contacts.objects.all()

   
    context = {
        'slider': slider,
        'category': category,
        'sale_product': sale_product,
        'new_product': new_product,
        'contacts': contacts
    }
    return render(request, 'content/index.html', context)




def all_products(request):
    all_products = Product.objects.all()
    category = Category.objects.all()
    contacts = Contacts.objects.all()
    

    context = {
        'all_products':all_products,
        'category': category,
        'contacts': contacts
    }
    return render(request, 'content/all_products.html', context)





def products(request, id):
    products = Product.objects.filter(category=id)
    category = Category.objects.all()
    contacts = Contacts.objects.all()



    context = {
        'products':products,
        'category': category,
        'contacts': contacts


    }
    return render(request, 'content/all_products.html', context)



def products_detail(request, id):
    products = Product.objects.all()
    product = products.filter(id=id) 
    category = Category.objects.all()
    product_one = products[:5]
    contacts = Contacts.objects.all()



    context = {
        'product':product,
        'category': category,
        'product_one': product_one,
        'contacts': contacts

    }
    return render(request, 'content/product_detail.html', context)


def contact(request):
    category = Category.objects.all()

    form = ContactUsForm()
    contacts = Contacts.objects.all()
    if request.method=="POST":
        form=ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {
        'category': category,
        
        'form': form,
        'contacts': contacts
    }
    return render(request, 'content/contact.html', context)



def about_us(request):
    about_us = About_us.objects.all()
    galleria = Galleria.objects.all()
    category = Category.objects.all()

    contacts = Contacts.objects.all()
    context = {
        'about_us': about_us,
        'galleria': galleria,
        'contacts': contacts,
        'category': category,

    }
    return render(request, 'content/about_us.html', context)
