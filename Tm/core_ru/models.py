from django.db import models



# фотография для слайдера

class Slider(models.Model):

    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Имя")
    image = models.ImageField(upload_to='slider', blank=True, null=True, verbose_name='Слайдер')
    is_active = models.BooleanField(default=False)
   


    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'

    def __str__(self):
        return self.name
    

# категория

class Category(models.Model):

    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Имя")
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to='category', blank=True, null=True, verbose_name='Категории')


    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name


# Продукт


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Какая категория подходит')
    sale = models.BooleanField(default=False, verbose_name='Акция')
    new =  models.BooleanField(default=False, verbose_name='Новый')


    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя")
    title = models.TextField(blank=True, null=True, verbose_name="Слоган")
    desc = models.TextField(blank=True, null=True, verbose_name="Описание")
    main_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Основная фотография')
    second_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Вторая фотография')
    three_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Третея фотография')

# первая таблица о продукте

    packing = models.CharField(max_length=255, blank=True, null=True, verbose_name='Упаковка')
    box_weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='Вес коробки')
    quantity_in_the_box = models.CharField(max_length=255, blank=True, null=True, verbose_name='Количество в коробке')
    shelf_life = models.CharField(max_length=255, blank=True, null=True, verbose_name='Дата истечения срока')

# вторая  таблица о продукте

    protein = models.CharField(max_length=255, blank=True, null=True, verbose_name='Белок')
    fat = models.CharField(max_length=255, blank=True, null=True, verbose_name='Жир')
    carbohydrate = models.CharField(max_length=255, blank=True, null=True, verbose_name='Углерод')
    the_energy_value = models.CharField(max_length=255, blank=True, null=True, verbose_name='Значение мощности')
    weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='Вес')



    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'



    def __str__(self):
        return self.name




# форма для отправки 

class ContactUs(models.Model):
    
    email = models.EmailField(max_length=50, verbose_name="Эл. адрес")
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=50, verbose_name="Мобильный телефон")
    message = models.TextField(verbose_name="SMS")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at",)


    class Meta:
        verbose_name = 'СМС'
        verbose_name_plural = 'СМС'


# фотографии о компании

class Galleria(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя")
    image = models.ImageField(upload_to='galleria', blank=True, null=True, verbose_name='Изображение для галереи')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Фотографии для галереи'


# о компании

class About_us(models.Model):

    title = models.CharField(max_length=255, verbose_name="Заявление")
    desc = models.TextField(verbose_name="О компании")
    main_image = models.ImageField(upload_to='about_us', blank=True, null=True, verbose_name='Баннер компании')
    second_image = models.ImageField(upload_to='about_us', blank=True, null=True, verbose_name='Профиль компании')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'Информация о компании'


# контакты 

class Contacts(models.Model):

    map = models.TextField( blank=True, null=True, verbose_name="Kartada ýerleşýän ýeriňiz")
    phone = models.CharField( blank=True, null=True, max_length=50, verbose_name='Номер телефона')
    email = models.EmailField( blank=True, null=True, verbose_name='Ваша электронная почта')
    address = models.CharField( blank=True, null=True, max_length=255, verbose_name='Адрес')
    header_logo = models.ImageField( blank=True, null=True, upload_to='header_logo', verbose_name='Логотип выше')
    footer_logo = models.ImageField( blank=True, null=True, upload_to='footer_logo', verbose_name='Логотип ниже')
    mini_desc = models.CharField( blank=True, null=True, max_length=255, verbose_name='Краткое описание')
    gmail = models.CharField( blank=True, null=True, max_length=255, verbose_name='Gmail')
    instagram = models.CharField( blank=True, null=True, max_length=255, verbose_name='Instagram')
    mail = models.CharField(  blank=True, null=True, max_length=255, verbose_name='Mail')
    tiktok = models.CharField( blank=True, null=True, max_length=255, verbose_name='TikTok')
 

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

