# Generated by Django 4.1.2 on 2022-10-30 14:31

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='image_url',
            field=models.ImageField(blank=True, default='images/8049189213.png', null=True, upload_to=web.models.upload_to),
        ),
    ]