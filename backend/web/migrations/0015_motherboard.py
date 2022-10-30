# Generated by Django 4.1.2 on 2022-10-30 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_storage_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=10)),
                ('name', models.CharField(default='', max_length=50)),
                ('size', models.CharField(default='', max_length=50)),
                ('allData', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='motherboard', to='web.alldata')),
            ],
        ),
    ]
