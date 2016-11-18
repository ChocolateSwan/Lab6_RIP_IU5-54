from django.db import models

# Create your models here.

class user_model (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    birthday = models.DateField(null=True, blank=True)
    tel_number = models.CharField(max_length=11, unique=True)
    in_black_list = models.BooleanField(default=0)
    ante_for = models.ForeignKey('ante_model', null=True)



class ante_model (models.Model):
    amount = models.FloatField()

class team_model (models.Model):
    name = models.CharField(max_length=255, unique=True)
    kind_of_sport = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    quantity_win = models.IntegerField(default=0)
    quantity_lose = models.IntegerField(default=0)