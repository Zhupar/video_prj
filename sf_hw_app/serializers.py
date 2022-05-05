from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    video_author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Video
        fields = ('caption', 'video', 'video_author', 'video_date_time', 'like')