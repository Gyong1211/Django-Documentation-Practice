from django.db import models
from utils.models.mixins import TimeStampedMixin


class Post(TimeStampedMixin):
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(TimeStampedMixin):
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    content = models.TextField()


class User(TimeStampedMixin):
    name = models.CharField(max_length=30)
