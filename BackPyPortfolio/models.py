import os
from django.db import models



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"logo-image/{final_name}"


            
    

class Section(models.Model):
    title=models.CharField(max_length=100)
    links=models.CharField(max_length=250)
    image=models.ImageField(upload_to=upload_image_path)
    active=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    