from rest_framework import serializers
from chaotix.tasks import generate_image_from_prompt
from celery import group

class ImageGeneratorSerializer(serializers.Serializer):
    """
    This Serializer class takes 5 prompts in the request
    body, if any of the prompts are empty it provides a
    default for that prompt.
    """
    prompt_1 = serializers.CharField(allow_blank=True)
    prompt_2 = serializers.CharField(allow_blank=True)
    prompt_3 = serializers.CharField(allow_blank=True)
    prompt_4 = serializers.CharField(allow_blank=True)
    prompt_5 = serializers.CharField(allow_blank=True)

    def validate(self, attrs):
        """
        provide a default prompt is any of the prompt is empty
        """
        default_prompt = ["A red flying dog", "A husky ninja", "A footballer kid", "A wizard on Mars", "Baby Dragon"]
        for i, k in enumerate(attrs):
            attrs[k] = default_prompt[i] if not bool(attrs[k]) else attrs[k]
        return attrs

    def create(self, validated_data):
        """
        run the generate image task in the background using celery
        """
        jobs = group(generate_image_from_prompt.s(v) for k,v in validated_data.items())
        res = jobs.apply_async()
        return validated_data


