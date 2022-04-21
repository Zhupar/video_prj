from django_filters import FilterSet, CharFilter, DateFilter
from django.forms import DateInput

from .models import Video


class VideoFilter(FilterSet):
    video_caption = CharFilter(field_name='caption', lookup_expr='icontains', label='caption')
    video_date_time = DateFilter(field_name='video_date_time', widget=DateInput(attrs={'type': 'date'}),
                                         lookup_expr='gt', label='later date')

    class Meta:
        model = Video
        fields = ['video_author',]