from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Subject(models.Model):
    topic = models.TextField()

    def __str__(self):
        return self.topic


class Post(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
