from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length=40)
    content = models.TextField()
    thumbnail = ProcessedImageField(
        upload_to="thumbnail/",
        blank=True,
        null=True,
        processors=[ResizeToFill(400, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
