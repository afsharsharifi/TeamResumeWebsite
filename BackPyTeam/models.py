from django.db import models
import os
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.first_name}{ext}"
    return f"logo-image/{final_name}"


class TeamMembers(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    position = models.CharField(max_length=80)
    photo = models.ImageField(upload_to=upload_image_path, blank=True, null=True,help_text="Image size: 245 × 247")
    personal_cv = models.CharField(max_length=150, unique=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
