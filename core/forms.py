from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(max_length=255)