# Generated by Django 3.2.2 on 2021-07-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackPySlider', '0004_alter_slider_middletext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='MiddleText',
            field=models.TextField(help_text='seprate your options with comma ( , ) ', max_length=300),
        ),
    ]
