from django.contrib import admin
from .models import Video, Comment, SubscribeIgnore


admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(SubscribeIgnore)
