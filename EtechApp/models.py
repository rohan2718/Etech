from click import DateTime
from django.db import models
import datetime

# Create your models here.

#contact Form
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    desc = models.TextField(max_length=300,default="")
    date = models.DateField(default=str(datetime.date.today()))

    def __str__(self):
        return self.email