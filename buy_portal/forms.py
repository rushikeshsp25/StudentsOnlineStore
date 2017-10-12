from django import forms
from django.contrib.auth.models import User
from . models import Item,Advertisement,Requirement

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=['category','item_name','mrp_price','selling_price','image','description']

class AdvertiseForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields=['title','image','description']

class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields=['title','expected_price','description']