from django import forms
from myapp.models import *

class FishForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = "__all__"

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

class HabitatForm(forms.ModelForm):
    class Meta:
        model = Habitat
        fields = "__all__"