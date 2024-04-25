from django.urls import path, include
from core.views import ImageGeneratorCreateViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'image-generator', ImageGeneratorCreateViewSet, basename="image_generator")

urlpatterns = [
    path('', include(router.urls))
]