from django.forms import ModelForm
from .models import Item, Home

class itemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'item_img','quantity']

class homeForm(ModelForm):
    class Meta:
        model = Home
        fields = ['name', 'house_pic', 'city']