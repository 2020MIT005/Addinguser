from django.db import models
from django.conf import settings
# Create your models here.
class Project(models.Model):
    name = models.TextField(blank=True)
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)
    date_created = models.DateTimeField(auto_now=True)
    

