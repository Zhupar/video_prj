from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from sf_hw_app.views import VideoViewSet

router = routers.DefaultRouter()
router.register(r'video', VideoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sf_hw_app.urls')),
    path('api/v1/', include(router.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
