from django.db import models

# Create your models here.


class ContactUs(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
