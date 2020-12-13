from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')

    def __str__(self):
        return self.name

class Startup(models.Model):
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')
    description = models.TextField()
    founded_date = models.DateField("date founded")
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class NewsLink(models.Model):
    title = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)
    pub_date = models.DateField("date published")
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.startup}:{self.title}"