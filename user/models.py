from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Vehicle(models.Model):
    CHOICES = (
        ('two_wheeler','Two wheeler',),
        ('four_wheeler','Four wheeler'),
    )
    type = models.CharField(max_length=30,choices=CHOICES)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)
    registration_number = models.CharField(max_length=15,unique=True,help_text='TN 07 AL 2406 - TEN DIGIT')
    date_of_registration = models.DateField(help_text='yyyy-mm-dd | mm-dd-yyyy')
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.owner_name

