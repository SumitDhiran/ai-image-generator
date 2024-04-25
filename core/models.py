from django.db import models

# Create your models here.


class ImageData(models.Model):
    base64 = models.TextField(null=True, blank=True)
    finish_reason = models.CharField(max_length=255, null=True, blank=True)
    seed = models.BigIntegerField(null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.pk}_{self.base64[:10]}_{self.finish_reason}_{str(self.seed)}"
