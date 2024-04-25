from rest_framework import viewsets, mixins, permissions, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from core.serializers import ImageGeneratorSerializer


class ImageGeneratorCreateViewSet(viewsets.GenericViewSet,
                               mixins.CreateModelMixin):
    """
    This CreateViewset generates 5 different images
    using stability.ai text-to-image API.
    uses celery tasks to parallelly generate all the images in the
    background
    returns: prompts with status code
    """

    serializer_class = ImageGeneratorSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

