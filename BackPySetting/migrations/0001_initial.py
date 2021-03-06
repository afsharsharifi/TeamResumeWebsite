# Generated by Django 3.2.5 on 2021-07-22 13:49

import BackPySetting.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=True, max_length=50)),
                ('about_text', models.TextField()),
                ('about_image', models.ImageField(blank=True, null=True, upload_to=BackPySetting.models.upload_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=BackPySetting.models.upload_image_path)),
                ('favicon', models.ImageField(blank=True, null=True, upload_to=BackPySetting.models.upload_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('telegram', 'telegram'), ('instagram', 'instagram'), ('github', 'github'), ('linkedin', 'linkedin'), ('facebook', 'facebook'), ('whatsapp', 'whatsapp'), ('twitter', 'twitter'), ('youtube', 'youtube'), ('pinterest', 'pinterest'), ('skype', 'skype'), ('dribbble', 'dribbble'), ('reddit', 'reddit'), ('stackoverflow', 'stackoverflow')], max_length=50)),
                ('tooltip', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=500)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
