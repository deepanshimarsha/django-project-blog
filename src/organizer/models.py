from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)

class Startup(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)
    description = models.TextField()
    founded_date = models.DateField()
    contact = models.EmailField()
    website = models.URLField()

class NewsLink(models.Model):
    title = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)
    pub_date = models.DateField()
    link = models.URLField()
