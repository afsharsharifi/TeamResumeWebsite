import os
from django.db import models

# Create your models here.

SocialOptions = (
    ('telegram', 'telegram'),
    ('instagram', 'instagram'),
    ('github', 'github'),
    ('linkedin', 'linkedin'),
    ('facebook', 'facebook'),
    ('whatsapp', 'whatsapp'),
    ('twitter', 'twitter'),
    ('youtube', 'youtube'),
    ('pinterest', 'pinterest'),
    ('skype', 'skype'),
    ('dribbble', 'dribbble'),
    ('reddit', 'reddit'),
    ('stack-overflow', 'stack-overflow')
)

ShareUsOptions = (
    ('telegram', 'telegram'),
    ('instagram', 'instagram'),
    ('whatsapp', 'whatsapp'),
    ('twitter', 'twitter'),
    ('pinterest', 'pinterest'),
    ('skype', 'skype'),
    ('reddit', 'reddit'),
)


StatusOptions = (
    ('ti-layers-alt', 'ti-layers-alt'),
    ('ti-map-alt', 'ti-map-alt'),
    ('fa fa-coffee', 'fa fa-coffee'),
    ('ti-face-smile', 'ti-face-smile'),
    ('ti-gallery', 'ti-gallery'),
    ('ti-agenda', 'ti-agenda'),
    ('ti-server', 'ti-server'),
    ('ti-stats-up', 'ti-stats-up'),
    ('ti-world', 'ti-world'),
    ('ti-bolt', 'ti-bolt'),
    ('ti-check', 'ti-check'),
    ('ti-check-box', 'ti-check-box'),
    ('ti-announcement', 'ti-announcement'),
    ('ti-eye', 'ti-eye'),
    ('ti-heart', 'ti-heart'),
    ('ti-pencil', 'ti-pencil'),
    ('ti-bookmark', 'ti-bookmark'),
    ('ti-desktop', 'ti-desktop'),
)


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"logo-image/{final_name}"


class Setting(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    logo = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True)
    favicon = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=50, default=True)
    about_text = models.TextField()
    about_image = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True)

    def __str__(self):
        return self.title


class SocialMedia(models.Model):
    title = models.CharField(max_length=50, choices=SocialOptions)
    link = models.CharField(max_length=500)
    tooltipshow = models.CharField(max_length=50)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.tooltipshow


class ShareUs(models.Model):
    title = models.CharField(max_length=50, choices=ShareUsOptions)
    link = models.CharField(max_length=500)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class Status(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, choices=StatusOptions)
    value = models.IntegerField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title