from django.db import models



# Post model created...extends models class from django.db
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

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


from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save

"""
class UserProfile(models.Model):
    # Links Account to a User model instance
    user = models.OneToOneField(User)

    # Additional attribute to the User
    # image = models.ImageField(upload_to='avatars', blank=True)  # requires PIL (Python Image Lib)
    role = models.CharField(max_length=10)

    def __unicode__(self):
        return self.username
"""
#create user object to attach to the Account object! Magi
# User.profile = property(lambda u: Account.objects.get_or_create(user=u)[0])



class Category(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places = 2)
    description = models.TextField(max_length=140)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name


class AuctionStatus(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Auction(models.Model):
    title = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
   # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    product = models.ForeignKey(Product)
    status = models.ForeignKey(AuctionStatus)

    #TODO Add foreign keys
    def __unicode__(self):
        return self.title



