from django.db import models



# фотография для слайдера

class Slider(models.Model):

    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ady")
    image = models.ImageField(upload_to='slider', blank=True, null=True, verbose_name='Slider')
    is_active = models.BooleanField(default=False)
   


    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliderler'

    def __str__(self):
        return self.name
    

# категория

class Category(models.Model):

    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ady")
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name="Beýany")
    image = models.ImageField(upload_to='category', blank=True, null=True, verbose_name='Kategoriyalar')


    class Meta:
        verbose_name = 'Kategoryia'
        verbose_name_plural = 'Kategoriyalar'


    def __str__(self):
        return self.name


# Продукт


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Haysy kategoriya degishliligi')
    sale = models.BooleanField(default=False)
    new =  models.BooleanField(default=False)


    name = models.CharField(max_length=255, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    main_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Esasy Haryt')
    second_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='ikinji Haryt')
    three_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='uchunji Haryt')

# первая таблица о продукте

    packing = models.CharField(max_length=255, blank=True, null=True, verbose_name='Gaplamak')
    box_weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='Gutynyň agramy')
    quantity_in_the_box = models.CharField(max_length=255, blank=True, null=True, verbose_name='Bir gutydaky mukdar')
    shelf_life = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ýaramlylyk möhleti')

# вторая  таблица о продукте

    protein = models.CharField(max_length=255, blank=True, null=True, verbose_name='Belok')
    fat = models.CharField(max_length=255, blank=True, null=True, verbose_name='Yag')
    carbohydrate = models.CharField(max_length=255, blank=True, null=True, verbose_name='Uglerod')
    the_energy_value = models.CharField(max_length=255, blank=True, null=True, verbose_name='Kuwwatlylyk gymmaty')
    weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='Agramy')



    class Meta:
        verbose_name = 'Haryt'
        verbose_name_plural = 'Harytlar'



    def __str__(self):
        return self.name




# форма для отправки 

class ContactUs(models.Model):
    
    email = models.EmailField(max_length=50, verbose_name="Email poçtasy")
    name = models.CharField(max_length=100, verbose_name="Ady")
    phone = models.CharField(max_length=50, verbose_name="El telefony")
    message = models.TextField(verbose_name="SMS")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at",)


    class Meta:
        verbose_name = 'SMS'
        verbose_name_plural = 'SMSLER'


# фотографии о компании

class Galleria(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ady")
    image = models.ImageField(upload_to='galleria', blank=True, null=True, verbose_name='Gallereýa üçin surat')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Galleria'
        verbose_name_plural = 'Galleria üçin suratlar'


# о компании

class About_us(models.Model):

    title = models.CharField(max_length=255, verbose_name="Beýan")
    desc = models.TextField(verbose_name="Kompaniýa barada")
    main_image = models.ImageField(upload_to='about_us', blank=True, null=True, verbose_name='Kompaniýa barada banner')
    second_image = models.ImageField(upload_to='about_us', blank=True, null=True, verbose_name='Kompaniýa barada surat')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kompaniýa barada'
        verbose_name_plural = 'Kompaniýa barada maglumatlar'


# контакты 

class Contacts(models.Model):

    map = models.TextField( blank=True, null=True, verbose_name="Kartada ýerleşýän ýeriňiz")
    phone = models.CharField( blank=True, null=True, max_length=50, verbose_name='Telefon belgi')
    email = models.EmailField( blank=True, null=True, verbose_name='Elektron poçtaňyz')
    address = models.CharField( blank=True, null=True, max_length=255, verbose_name='Adress')
    header_logo = models.ImageField( blank=True, null=True, upload_to='header_logo', verbose_name='Ýokardaky logo')
    footer_logo = models.ImageField( blank=True, null=True, upload_to='footer_logo', verbose_name='Aşakdaky logo')
    mini_desc = models.CharField( blank=True, null=True, max_length=255, verbose_name='Gysgaça beýan')
    gmail = models.CharField( blank=True, null=True, max_length=255, verbose_name='Gmail')
    instagram = models.CharField( blank=True, null=True, max_length=255, verbose_name='Instagram')
    mail = models.CharField(  blank=True, null=True, max_length=255, verbose_name='Mail')
    tiktok = models.CharField( blank=True, null=True, max_length=255, verbose_name='TikTok')
 

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Kontakt'
        verbose_name_plural = 'Kontaktlar'

