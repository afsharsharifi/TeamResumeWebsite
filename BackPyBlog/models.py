from django.db import models
from django.db.models.fields import CharField, IntegerField
import os
from django import forms
from django.forms import widgets

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"logo-image/{final_name}"

class Blog(models.Model):
    title = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    blog_content = models.TextField()
    write = CharField(max_length=150)
    visit_count = IntegerField()
    share = CharField(max_length=500)
    link_content = CharField(max_length=200)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True,help_text="Image size: 360 × 240")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    