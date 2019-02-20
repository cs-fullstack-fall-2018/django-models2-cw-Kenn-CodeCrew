from django.db import models

# Create your models here.
class Respondent(models.Model):
    respondent_name = models.CharField(max_length=50)
    respondent_age = models.IntegerField()
    respondent_income = models.IntegerField()