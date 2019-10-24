
from django.db import models


# Create your models here.
class approvals(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    age = models.IntegerField()
    sex = models.IntegerField()
    chest = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restcg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.IntegerField()

