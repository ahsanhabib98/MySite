from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput, required=True)
    subject = forms.CharField(widget=forms.TextInput, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
