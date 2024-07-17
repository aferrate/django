from django.db import models

class Requests(models.Model):
    name_company = models.CharField(max_length=255)
    date = models.DateField()