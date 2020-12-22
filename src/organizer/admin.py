from django.contrib import admin
from .models import Startup, Tag, NewsLink

# Register your models here.
admin.site.register(NewsLink)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ("name", "slug")

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):

    list_display = ("name", "slug")
    prepopulated_fields = {"slug":("name",)}

