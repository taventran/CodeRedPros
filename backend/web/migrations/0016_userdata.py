# Generated by Django 4.1.2 on 2022-10-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_motherboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.IntegerField(default=1)),
                ('aesthetics', models.BooleanField(default=False)),
                ('priceRange', models.FloatField(default=10)),
                ('size', models.IntegerField(default=1)),
            ],
        ),
    ]
