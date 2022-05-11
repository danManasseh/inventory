from django.forms import ModelForm
from .models import Item

class itemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'item_img','quantity']