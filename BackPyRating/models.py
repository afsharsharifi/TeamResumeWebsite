from django.db import models
import os
# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.clint_name}{ext}"
    return f"logo-image/{final_name}"



StarsOptions = (
    ('★★★★★', 'five_star'),
    ('★★★★', 'four_star'),
    ('★★★', 'three_star'),
    ('★★', 'two_star'),
    ('★', 'one_star'),
)

class Rating(models.Model):
    clint_name = models.CharField(max_length=150)
    rating = models.CharField(max_length=150, choices=StarsOptions)
    comment = models.TextField()
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)

    def __str__(self):
        return self.clint_name
