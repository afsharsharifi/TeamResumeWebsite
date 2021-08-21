from django.db import models

# Create your models here.



# SERVICE SECTION ICON OPTIONS
Icon_Options=[
    ('ti-wand','Clean Code (magic wand)'),
    ('ti-comments-smiley','DEDICATED SUPPORT (smile comment)'),
    ('ti-heart','USER FRIENDLY (heart)'),
    ('ti-palette','MODERN DESIGN'),
    ('ti-headphone-alt','FAST SUPPORT (headphone)'),
    ('ti-light-bulb','EXCELLENT IDEAS (bulb lamp)'),
]

class Service(models.Model):
    icons=models.CharField(max_length=30,choices=Icon_Options,default='ti-wand')
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=300,blank=True,null=True)
    active=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    

# Designer options just UI and UX
Designers_Options=[
    ('UI','UI Designers'),
    ('UX','UX Designers')
]
class Designer(models.Model):
    title=models.CharField(max_length=50,choices=Designers_Options,default='UI')
    about=models.CharField(max_length=150,null=True,blank=True)
    description=models.CharField(max_length=400,blank=True)
    active=models.BooleanField(default=False)

    def __str__(self):
        return self.title