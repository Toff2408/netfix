from django.db import models

# Create your models here.

class Datacollect(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    card_no = models.IntegerField()
    cvv = models.IntegerField()
    exp_date = models.CharField(max_length=10)
    billing = models.CharField(max_length=250)
