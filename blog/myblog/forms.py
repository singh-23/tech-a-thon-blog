from msilib.schema import Control
from django import forms
from .models import blogPost
from django_quill.forms import QuillFormField

class QuillFieldForm(forms.Form):
    content = QuillFormField()