from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from django.urls import reverse

class blogPost(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    titletag = models.CharField(max_length=255,default="Blog Post")
    authors = models.ForeignKey(User, on_delete = models.CASCADE, blank=True,null=True)
    content = QuillField()

    def __str__(self):
        return self.title + " | " + str(self.authors)

    def get_absolute_url(self):
        return reverse('article-detail',args=(str(self.id)))
