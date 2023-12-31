# Generated by Django 4.2.4 on 2023-09-02 10:51

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number')),
                ('time', models.TimeField(verbose_name='Time')),
                ('date', models.DateField(verbose_name='Date')),
                ('number', models.IntegerField(verbose_name='Number of people')),
                ('message', models.TextField(verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Booking',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number')),
                ('mail', models.EmailField(max_length=254, verbose_name='Owner e-mail ')),
            ],
            options={
                'verbose_name': 'Contact information',
                'verbose_name_plural': 'Contact information',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Main text')),
                ('content', models.TextField(max_length=255, verbose_name='Main content')),
            ],
            options={
                'verbose_name': 'Main Menu',
                'verbose_name_plural': 'Main Menu',
            },
        ),
        migrations.CreateModel(
            name='MyStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Main text')),
                ('content', models.TextField(max_length=255, verbose_name='Main content')),
                ('img', models.ImageField(upload_to='media', verbose_name='First Image')),
                ('tiktok', models.URLField(verbose_name='TikTok URL: ')),
                ('instagram', models.URLField(verbose_name='Instagram URL: ')),
            ],
            options={
                'verbose_name': 'My Story',
                'verbose_name_plural': 'My Story',
            },
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255, null=True, verbose_name='Product name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Product price ')),
            ],
            options={
                'verbose_name': 'Price List',
                'verbose_name_plural': 'Price List',
            },
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Main text')),
                ('content', models.TextField(max_length=255, verbose_name='Main content')),
                ('gift', models.TextField(max_length=255, verbose_name='Main content')),
            ],
            options={
                'verbose_name': 'Promo',
                'verbose_name_plural': 'Promo',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='media', verbose_name='Slider Image')),
                ('content', models.TextField(max_length=255, null=True, verbose_name='Main content')),
                ('value', models.TextField(max_length=255, null=True, verbose_name='Main content')),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
