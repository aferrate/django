from django.db import models

class Call(models.Model):
    name_company = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)