# Generated by Django 4.1.2 on 2022-10-30 12:58

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_userdata_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='image_url',
            field=models.ImageField(blank=True, default='images/smile_face.jpeg', null=True, upload_to=web.models.upload_to),
        ),
    ]