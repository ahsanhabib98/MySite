from django import forms
from django.forms import TextInput
from .models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        widgets = {
            'email': TextInput(attrs={'class':'form-control'}),
        }
