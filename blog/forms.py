from django import forms
from .models import PostModel


class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = '__all__'
        exclude = ['draft', 'slug', 'publish_date', 'read_time', ]
