from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    number_of_pages = models.IntegerField(unique=False)
    year_of_publication = models.IntegerField(unique=False)

