""" Development of Web Applications and Web Services

"""

__author__ = "Dawit Nida (dawit.nida@abo.fi)"
__date__ = "Date: 1.10.2014"
__version__ = "Version: "

from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from myblog.models import Post, User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=False, max_length=100)
    last_name = forms.CharField(required=False, max_length=100)
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
