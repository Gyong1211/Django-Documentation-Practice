"""
Post모델
    author
    title
    content
    created_date
    modified_date

Comment모델
    author = User와 연결
    post = Post와 연결
    content
    created_date
    modified_date

User모델
    name
    created_date

"""
from django.db import models


class TimeStampedMixin(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True