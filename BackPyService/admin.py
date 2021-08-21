from django.contrib import admin
from django.db.models.base import Model

# Register your models here.
from .models import Service,Designer

class ServideAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title' ,'active']

    class Meta:
        model = Designer

admin.site.register(Service)
admin.site.register(Designer)