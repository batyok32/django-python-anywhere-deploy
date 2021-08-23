from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.core.files.storage import default_storage

# Create your models here.

class Slider(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=150, default="/")
    image = models.ImageField(upload_to='sliders/%Y/%m/%d', blank=True, default="product_default.jpg")
    picture = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1920, 450)],
        format="WebP",
        options={"quality":100},
    )
    picture_admin = ImageSpecField(
        source="image",
        processors=[ResizeToFill(200, 70)],
        format="WebP",
        options={"quality":100},
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

   
    def delete(self, *args, **kwargs):
        from django.core.files.storage import default_storage
        if self.image:
            with contextlib.suppress(FileNotFoundError):
                default_storage.delete(
                    self.picture.path
                )
            self.image.delete()
        super().delete(*args, **kwargs)