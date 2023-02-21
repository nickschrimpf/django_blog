from django.contrib import admin
from .models import Author, Post ,Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title","author","date")
    list_filter = ("title","date","tags","author")

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post,PostAdmin)
