from django import forms
from django.forms import ModelForm

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']
        labels = {
            'full_name': '',
            'subject': 'Subject:',
            'email': '',
            'message': '',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control \
                text-mute mb-3', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control \
                mb-3', 'placeholder': 'Email'}),
            'subject': forms.Select(attrs={'class': 'form-check-inline \
                list-unstyled mb-3 text-dark text-mute ml-2'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Write message'}),
         }