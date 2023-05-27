from django.db import models
from datetime import datetime

# Contact model


class Contact(models.Model):
    SUBJECT_CHOICES = (
        ('1', 'Info'),
        ('2', 'Warranties'),
        ('3', 'Complaints')

    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    subject = models.CharField(choices=SUBJECT_CHOICES,
                               max_length=100, default=1)
    message = models.TextField(max_length=3000)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# Designers model


class Designer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    hierarchy = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    facebook_link = models.URLField(max_length=100)
    twiter_link = models.URLField(max_length=100) 

    def __str__(self):
        return (f"{self.first_name}  {self.last_name}")
