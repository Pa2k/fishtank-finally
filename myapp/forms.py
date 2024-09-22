from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]


class FishForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = '__all__'

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_type', 'food_name', 'feeding_frequency', 'food_source']

class HabitatForm(forms.ModelForm):
    class Meta:
        model = Habitat
        fields = ['habitat_name','temperature','ph_level','migration']