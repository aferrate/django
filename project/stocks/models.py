from django.db import models
from datetime import date

class Requests(models.Model):
    name_company = models.CharField(max_length=255)
    date_start = models.DateField(_("Date"))
    date_end = models.DateField(_("Date"))