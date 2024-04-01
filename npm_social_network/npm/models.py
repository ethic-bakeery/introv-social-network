import datetime
from django.db import models
from django.utils import timezone

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    local_gov = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()

class Room(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, through='RoomMembership', related_name='rooms')

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    is_admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

class RoomMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

class Page(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=100)
    followers = models.ManyToManyField(User, through='PageFollow', related_name='pages')

class PageFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    dateTime = models.DateTimeField()
    comment = models.TextField()
    like = models.IntegerField()
    lage = models.ForeignKey('Page', on_delete=models.CASCADE, related_name='posts')

class Admin(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    local_gov = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='admins')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='admins')
    followers = models.IntegerField()
    profession = models.CharField(max_length=100)
