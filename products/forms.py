from django import forms
from django.contrib.auth.models import User
from .widgets import CustomClearableFileInput
from .models import Product, Category, Customise
from user_profile.models import UserProfile
from django.forms import ModelChoiceField

# Copied from BoutiqueAdo


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "Product #%s %s / %s" % (obj.id, obj.name, obj.category)


class CustomiseForm(forms.ModelForm):
    product = ProductModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = Customise
        exclude = ('created_date',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field

        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_name': 'Username',
            'email': 'Email',
            'phone_number': 'Phone_number',
            'product': 'Choose Product',
            'sole': 'Choose Sole',
            'color': 'Chose Color',
            'logo': '',
            'special_size': 'Choose Size',
            'details': 'Write here some specific requirements.'
        }

        self.fields['product'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != ['sole', 'color', 'special_size', 'product']:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black \
                rounded-0 profile-form-input'
