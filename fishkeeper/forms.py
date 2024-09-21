from django import forms
from myapp.models import *

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