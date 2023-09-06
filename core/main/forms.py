from django import forms
from django.forms import ModelForm
from .models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'