from django.db import models
from django.contrib.auth.models import User


class SubscribeIgnore(models.Model):
    subscriber = models.ManyToManyField(User, related_name='subscribers', verbose_name='subscribers')
    ignore = models.ManyToManyField(User, related_name='ignore', verbose_name='ignore')

    def __str__(self):
        return self.site_user


class Video(models.Model):
    caption = models.CharField(max_length=250, default="caption", verbose_name='caption')
    video = models.FileField(upload_to="video/", verbose_name='video')
    like = models.IntegerField(default=0, verbose_name='like')
    video_author = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user_name')
    video_date_time = models.DateTimeField(auto_now_add=True, verbose_name='video_date_time')

    def __str__(self):
        return self.caption

    def video_like(self):
        self.like += 1
        self.save()


class Comment(models.Model):
    com_video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name='com_post')
    com_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='com_user')
    com_text = models.TextField(verbose_name='com_text')
    com_date_time = models.DateTimeField(auto_now_add=True, verbose_name='com_date_time')

