from django import forms
from .models import Address
from django.forms import fields


class StoreData(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
