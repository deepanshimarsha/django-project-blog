from django.db import models
from organizer.models import Tag, Startup

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)

    def __str__(self):
        date_string = self.pub_date.strftime("%y-%m-%d")
        return f"(self.title} on {date_string}"