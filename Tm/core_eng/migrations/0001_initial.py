# Generated by Django 4.0.6 on 2022-08-07 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Statement')),
                ('desc', models.TextField(verbose_name='About company')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='about_us', verbose_name='Company banner')),
                ('second_image', models.ImageField(blank=True, null=True, upload_to='about_us', verbose_name='Company Profile')),
            ],
            options={
                'verbose_name': 'About company',
                'verbose_name_plural': 'About company',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map', models.TextField(blank=True, null=True, verbose_name='Kartada ýerleşýän ýeriňiz')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('header_logo', models.ImageField(blank=True, null=True, upload_to='header_logo', verbose_name='Logo above')),
                ('footer_logo', models.ImageField(blank=True, null=True, upload_to='footer_logo', verbose_name='Logo below')),
                ('mini_desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mini description')),
                ('gmail', models.CharField(blank=True, max_length=255, null=True, verbose_name='Gmail')),
                ('instagram', models.CharField(blank=True, max_length=255, null=True, verbose_name='Instagram')),
                ('mail', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mail')),
                ('tiktok', models.CharField(blank=True, max_length=255, null=True, verbose_name='TikTok')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ContactUs',
                'verbose_name_plural': 'ContactUs',
            },
        ),
        migrations.CreateModel(
            name='Galleria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='galleria', verbose_name='Image for gallery')),
            ],
            options={
                'verbose_name': 'Galleria',
                'verbose_name_plural': 'Galleria',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slider', verbose_name='Slider')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.BooleanField(default=False, verbose_name='Sale')),
                ('new', models.BooleanField(default=False, verbose_name='NEW')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Title')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Main image')),
                ('second_image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Second image')),
                ('three_image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Three image')),
                ('packing', models.CharField(blank=True, max_length=255, null=True, verbose_name='Packing')),
                ('box_weight', models.CharField(blank=True, max_length=255, null=True, verbose_name='Box weight')),
                ('quantity_in_the_box', models.CharField(blank=True, max_length=255, null=True, verbose_name='Quantity in the box')),
                ('shelf_life', models.CharField(blank=True, max_length=255, null=True, verbose_name='Shelf life')),
                ('protein', models.CharField(blank=True, max_length=255, null=True, verbose_name='Protein')),
                ('fat', models.CharField(blank=True, max_length=255, null=True, verbose_name='Fat')),
                ('carbohydrate', models.CharField(blank=True, max_length=255, null=True, verbose_name='Carbohydrate')),
                ('the_energy_value', models.CharField(blank=True, max_length=255, null=True, verbose_name='The_energy_value')),
                ('weight', models.CharField(blank=True, max_length=255, null=True, verbose_name='Weight')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_eng.category', verbose_name='Which category is suitable')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]