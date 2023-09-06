from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class HomePage(models.Model):
    title = models.CharField('Main text', max_length=255)
    content = models.TextField('Main content', max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Main Menu'
        verbose_name_plural = 'Main Menu'

class MyStory(models.Model):
    title = models.CharField('Main text', max_length=255)
    content = models.TextField('Main content', max_length=255)
    img = models.ImageField("First Image" , upload_to='media')
    tiktok = models.URLField('TikTok URL: ')
    instagram = models.URLField('Instagram URL: ')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'My Story'
        verbose_name_plural = 'My Story'

class Promo(models.Model):
    title = models.CharField('Main text', max_length=255)
    content = models.TextField('Main content', max_length=255)
    gift = models.TextField('Main content', max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Promo'
        verbose_name_plural = 'Promo'

class Services(models.Model):
    img = models.ImageField("Slider Image" , upload_to='media' , null=True)
    content = models.TextField('Main content', max_length=255 , null=True)
    value = models.TextField('Price', max_length=255 , null=True)

    def __str__(self) -> str:
        return self.content
    
    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'

class Booking(models.Model):

    name = models.CharField('Name', max_length=255)
    phone = PhoneNumberField("Phone Number" )
    time = models.TimeField("Time")
    date = models.DateField("Date")
    number = models.IntegerField("Number of people")
    message = models.TextField("Comment")

    def __str__(self) -> str:
        return "Booking"
    
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking'

class PriceList(models.Model):
    product = models.CharField('Product name', max_length=255 , null=True)
    price = models.DecimalField('Product price ', decimal_places=2, max_digits=6, null=True)

    def __str__(self) -> str:
        return self.product
    
    class Meta:
        verbose_name = 'Price List'
        verbose_name_plural = 'Price List'

class ContactUs(models.Model):
    phone = PhoneNumberField("Phone Number")
    mail = models.EmailField('Owner e-mail')

    def __str__(self) -> str:
        return "ContactUs"

    class Meta:
        verbose_name = 'Contact information'
        verbose_name_plural = 'Contact information'
        db_table = 'contactus'  