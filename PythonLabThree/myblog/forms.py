""" Development of Web Applications and Web Services

"""

__author__ = "Dawit Nida (dawit.nida@abo.fi)"
__date__ = "Date: 1.10.2014"
__version__ = "Version: "

from django.forms import ModelForm
from myblog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post