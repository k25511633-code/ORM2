from django.db import models
from django.contrib import admin
class Carnumapp(models.Model):
    car_name = models.CharField()
    car_number = models.IntegerField()
    release_date = models.DateField()
    car_colour = models.CharField()


class CarnumAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_number', 'release_date', 'car-colour')
# Create your models here.
