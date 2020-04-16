from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    posted_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post-list')
