# Generated by Django 4.0.6 on 2022-07-28 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Kategoriyalar')),
                ('back_flip_image', models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Kategoriyalar')),
            ],
            options={
                'verbose_name': 'Kategoryia',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='slider', verbose_name='Slider')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliderler',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Esasy Haryt')),
                ('second_image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='ikinji Haryt')),
                ('three_image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='uchunji Haryt')),
                ('packing', models.CharField(blank=True, max_length=255, null=True)),
                ('box_weight', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity_in_the_box', models.CharField(blank=True, max_length=255, null=True)),
                ('shelf_life', models.CharField(blank=True, max_length=255, null=True)),
                ('protein', models.CharField(blank=True, max_length=255, null=True)),
                ('fat', models.CharField(blank=True, max_length=255, null=True)),
                ('carbohydrate', models.CharField(blank=True, max_length=255, null=True)),
                ('the_energy_value', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='Haysy kategoriya degishliligi')),
            ],
            options={
                'verbose_name': 'Haryt',
                'verbose_name_plural': 'Harytlar',
            },
        ),
    ]
