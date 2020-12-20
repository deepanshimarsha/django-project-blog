from django.db import models
from organizer.models import Tag, Startup
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField("date published", default = datetime.date.today)
    tags = models.ManyToManyField(Tag, related_name="blog_posts")
    startups = models.ManyToManyField(Startup, related_name="blog_posts")

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date", "title"]
        verbose_name = "blog post"

    def __str__(self):
        date_string = self.pub_date.strftime("%y-%m-%d")
        return f"{self.title} on {date_string}"