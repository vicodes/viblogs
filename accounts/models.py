from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='userprofile')
    photo = models.ImageField(upload_to='profile_images',blank=True,default="user2.png")
    website = models.URLField(null=True, blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
