from django.views.generic import ListView
from rest_framework import generics

from .filters import VideoFilter

from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import *
from .serializers import VideoSerializer
from .permissions import IsOwnerOrReadOnly


class VideoViewSet(viewsets.ModelViewSet):

    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsOwnerOrReadOnly]


# class VideoListApi(generics.ListCreateAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer
# class VideoList(ListView):
#     model = Video
#     template_name = 'index.html'
#     context_object_name = 'video'
#     queryset = Video.objects.order_by('-video_date_time')
#     paginate_by = 10
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
#
class Search(ListView):
    model = Video
    template_name = 'search.html'
    context_object_name = 'video'
    ordering = ['-video_date_time']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = VideoFilter(self.request.GET, queryset=self.get_queryset())
        return context


def index(request):
    video = Video.objects.all().order_by("-video_date_time")
    return render(request, "index.html", {"video": video})

