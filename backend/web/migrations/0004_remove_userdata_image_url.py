# Generated by Django 4.1.2 on 2022-10-30 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_userdata_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='image_url',
        ),
    ]
