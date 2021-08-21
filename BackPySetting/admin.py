from django.contrib import admin
from django.db.models.base import Model

# Register your models here.
from .models import Setting, About, SocialMedia, ShareUs, Status

admin.site.register(Setting)
admin.site.register(About)
admin.site.register(SocialMedia)
admin.site.register(ShareUs)
admin.site.register(Status)
