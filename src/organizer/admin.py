from django.contrib import admin
from .models import Startup, Tag, NewsLink

# Register your models here.
admin.site.register(Startup)
admin.site.register(Tag)
admin.site.register(NewsLink)
