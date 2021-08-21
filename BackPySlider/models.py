import os
from django.db import models

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"logo-image/{final_name}"

class Slider(models.Model):
    title=models.CharField(max_length=100,default='slider')
    BeforeText=models.CharField(max_length=20)
    MiddleText=models.TextField(max_length=300, help_text='seprate your options with comma ( , ) ')
    AfterText=models.CharField(max_length=20)
    UnderText=models.CharField(max_length=20,default='welcome')
    Description=models.CharField(max_length=100,blank=True,null=True)
    GoButton=models.CharField(max_length=10)
    SliderImage=models.ImageField(upload_to=upload_image_path,blank=True,null=True)

    def __str__(self):
        return self.title
    
