from django.db import models
from django.contrib.auth.models import User


# Post model created...extends models class from django.db
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, verbose_name="author")

    def __unicode__(self):
        return self.title

    @classmethod
    def exists(cls, pid):
        return len(cls.objects.filter(id=pid)) > 0

    @classmethod
    def getPostByID(cls, pid):
        try:
            return cls.objects.get(id=pid)
        except IndexError:
            return None

    @classmethod
    def fetchAllPosts(cls):
        try:
            queryset = cls.objects.all().order_by("-timestamp")[:10]
            return queryset
        except IndexError:
            return None


