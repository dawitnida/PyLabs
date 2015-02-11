""" Development of Web Applications and Web Services

"""

__author__ = "Dawit Nida (dawit.nida@abo.fi)"
__date__ = "Date: 25.10.2014"
__version__ = "Version: "


from rest_framework import serializers
from myblog.models import Post


class PostSerializer(serializers.ModelSerializer):
    b_author = serializers.RelatedField(source='author')

    class Meta:
        model = Post
        fields = ('title', 'content', 'timestamp', 'author')
