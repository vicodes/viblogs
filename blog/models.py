from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    body  = models.TextField()
    date  = models.DateTimeField(auto_now_add=True)
    likes  = models.ManyToManyField(User, related_name='likes',blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None)

    # def snippet(self):
    #     return self.body[:50]+"...."
    def __str__(self):
        return self.title
