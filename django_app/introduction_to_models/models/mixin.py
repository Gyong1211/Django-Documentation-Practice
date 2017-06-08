from django.db import models
from utils.models.mixins import TimeStampedMixin


class Post(TimeStampedMixin):
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    like_users = models.ManyToManyField(
        'User',
        through='PostLike',
        related_name='like_posts'
    )
    tag = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    def like_post(self, user):
        return PostLike.objects.create(user=user, post=self)

    def add_tag(self, tag_name):
        return


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

    def __str__(self):
        return self.name


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}의 Post {}에 대한 {}의 좋아요! {}'.format(
            self.post.author.name,
            self.post.title,
            self.user.name,
            self.created_date,
        )

    # class Meta:
    #     db_table = 'introduction_to_models_post_like_users'


class Tag(models.Model):
    title = models.CharField(max_length=50)
