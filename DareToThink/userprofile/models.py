from django.db import models
from django.contrib.auth.models import User
from DareToThink.settings import MEDIA_ROOT
import os

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    picture = models.ImageField(upload_to=MEDIA_ROOT+'/profileimages/', blank=True, null=True)
    location = models.TextField()
    gender = models.TextField()
    dateofbirth = models.TextField()
    special = models.TextField()

    #user.groups.add('normal_users',)

    # Override the __unicode__() method to return out something meaningful!

    #def picture(self):
    #    return os.path.basename(self.file.name)

    #def clean(self):
    #    return os.path.basename(self.file.name)
    #class Book(models.Model):
    #title = models.CharField(max_length=100)

    #@classmethod
    #def create():
    #    UserProfile.
    #    # do something with the book
    #    return UserProfile





class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    body = models.TextField()

    def __str__(self):
        return "%s (%s)" % (self.title, self.author)

class Motion(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)

class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    motion = models.ForeignKey(Motion)
    yes = models.IntegerField(default=0)
    no = models.IntegerField(default=0)
    maybe = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))


