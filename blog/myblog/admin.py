from django.contrib import admin
from .models import blogPost

@admin.register(blogPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass

