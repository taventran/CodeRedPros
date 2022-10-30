# Generated by Django 4.1.2 on 2022-10-29 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_remove_cpu_type_remove_cpucooler_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpucooler',
            name='allData',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='CPUCooler', to='web.alldata'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='allData',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='GPU', to='web.alldata'),
        ),
        migrations.AlterField(
            model_name='powersupply',
            name='allData',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='powerSupply', to='web.alldata'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='allData',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='storage', to='web.alldata'),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('name', models.TextField(blank=True, max_length=50)),
                ('allData', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='case', to='web.alldata')),
            ],
        ),
    ]
