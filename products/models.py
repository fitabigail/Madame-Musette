from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from home.models import Designer
from user_profile.models import UserProfile


# PRODUCT CATEGORIES MODEL


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

# PRODUCT MODEL


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_like", null=True)
    name = models.CharField(max_length=254)
    description = RichTextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image = models.ImageField(null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    is_customised = models.BooleanField(default=False)
    designer_id = models.ForeignKey(Designer, on_delete=models.PROTECT,
                                    blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(
        User, related_name='product_liked', blank=True)

    def __str__(self):
        return self.name

# PRODUCT CUSTOMISED MODEL


customised_sole = (
    ('platform', 'platform'),
    ('wedge heels', 'wedge heels')

)

customised_color = (
    ('beign', 'beign'),
    ('burgundy', 'burgundy'),
    ('red', 'red'),
    ('nude', 'nude')
)

customised_special_size = (
    ('UK 3', 'UK 3'),
    ('UK 3.5', 'UK 3.5'),
    ('UK 4', 'UK 4'),
    ('UK 4.5', 'UK 4.5'),
    ('UK 5', 'UK 5'),
    ('UK 5.5', 'UK 5.5'),
    ('UK 6', 'UK 6'),
    ('UK 6.5', 'UK 6.5'),
    ('UK 7', 'UK 7'),
    ('UK 7.5', 'UK 7.5'),
    ('UK 8', 'UK 8'),
    ('UK 8.5', 'UK 8.5'),
    ('UK 9', 'UK 9'),
    ('UK 9', 'UK 9'),
)


class Customise(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="custom_name",
        null=True)
    email = models.EmailField(max_length=100,
                              null=True)
    phone_number = models.CharField(max_length=20,
                                    null=True, blank=True)
    sole = models.CharField(max_length=150,
                            choices=customised_sole)
    color = models.CharField(max_length=150,
                             choices=customised_color)
    logo = models.BooleanField(default=False)
    special_size = models.CharField(max_length=150,
                                    choices=customised_special_size)
    details = models.TextField(blank=True)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}: Your request will be reviewed soon, \
            and we will replay by email."
