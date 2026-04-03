from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    # User o‘zidan boshqa foydalanuvchilarga obuna bo‘ladi
    user_subscribers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_subscribed_to',
        blank=True

    )

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/', default='videos/default.mp4')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    video_subscribers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="video_subscriptions",
        blank=True
    )

    def __str__(self):
        return self.title

    def subscriber_count(self):
        return self.video_subscribers.count()

class VideoComment(models.Model):
    video = models.ForeignKey('Video', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:30]}"

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscriptions', blank=True)

    def __str__(self):
        return self.user.username

class Subscription(models.Model):
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='author_subscriptions',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='author_subscribers',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('subscriber', 'author')
