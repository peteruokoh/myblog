from .models import Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

