from django.db import models
from django.contrib.auth.models import User



# фотография для слайдера

class Slider(models.Model):

    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Name")
    image = models.ImageField(upload_to='slider', blank=True, null=True, verbose_name='Slider')
    is_active = models.BooleanField(default=False)
   


    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.name
    

# категория

class Category(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Name")
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name="Description")
    image = models.ImageField(upload_to='category', blank=True, null=True, verbose_name='Category')


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name


# Продукт


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Which category is suitable')
    sale = models.BooleanField(default=False, verbose_name='Sale')
    new =  models.BooleanField(default=False, verbose_name='NEW')


    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")
    title = models.TextField(blank=True, null=True, verbose_name="Title")
    desc = models.TextField(blank=True, null=True, verbose_name="Description")
    main_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Main image')
    second_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Second image')
    three_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Three image')

# первая таблица о продукте

    packing = models.CharField(max_length=255, blank=True, null=True, verbose_name='Packing')
    box_weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='Box weight')
    quantity_in_the_box = models.CharField(max_length=255, blank=True, null=True, verbose_name='Quantity in the box')
    shelf_life = models.CharField(max_length=255, blank=True, null=True, verbose_name='Shelf life')

# вторая  таблица о продукте

    protein = models.CharField(max_length=255, blank=True, null=True, verbose_name='Protein')
    fat = models.CharField(max_length=255, blank=True, null=True, verbose_name='Fat')
    carbohydrate = models.CharField(max_length=255, blank=True, null=True, verbose_name='Carbohydrate')
    the_energy_value = models.CharField(max_length=255, blank=True, null=True, verbose_name='The_energy_value')
    weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='Weight')



    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'



    def __str__(self):
        return self.name




# форма для отправки 

class ContactUs(models.Model):
    
    email = models.EmailField(max_length=50, verbose_name="Email")
    name = models.CharField(max_length=100, verbose_name="Name")
    phone = models.CharField(max_length=50, verbose_name="Phone")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at",)


    class Meta:
        verbose_name = 'SMS'
        verbose_name_plural = 'SMS'


# фотографии о компании

class Galleria(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")
    image = models.ImageField(upload_to='galleria', blank=True, null=True, verbose_name='Image for gallery')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Galleria'
        verbose_name_plural = 'Galleria'


# о компании

class About_us(models.Model):

    title = models.CharField(max_length=255, verbose_name="Statement")
    desc = models.TextField(verbose_name="About company")
    main_image = models.ImageField(upload_to='about_us', blank=True, null=True, verbose_name='Company banner')
    second_image = models.ImageField(upload_to='about_us', blank=True, null=True, verbose_name='Company Profile')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About company'
        verbose_name_plural = 'About company'


# контакты 

class Contacts(models.Model):

    map = models.TextField( blank=True, null=True, verbose_name="Kartada ýerleşýän ýeriňiz")
    phone = models.CharField( blank=True, null=True, max_length=50, verbose_name='Phone number')
    email = models.EmailField( blank=True, null=True, verbose_name='Email')
    address = models.CharField( blank=True, null=True, max_length=255, verbose_name='Address')
    header_logo = models.ImageField( blank=True, null=True, upload_to='header_logo', verbose_name='Logo above')
    footer_logo = models.ImageField( blank=True, null=True, upload_to='footer_logo', verbose_name='Logo below')
    mini_desc = models.CharField( blank=True, null=True, max_length=255, verbose_name='Mini description')
    gmail = models.CharField( blank=True, null=True, max_length=255, verbose_name='Gmail')
    instagram = models.CharField( blank=True, null=True, max_length=255, verbose_name='Instagram')
    mail = models.CharField(  blank=True, null=True, max_length=255, verbose_name='Mail')
    tiktok = models.CharField( blank=True, null=True, max_length=255, verbose_name='TikTok')
 

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

