# Generated by Django 4.1.7 on 2023-05-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0036_alter_data_rain_alter_data_wind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='FWI',
            field=models.FloatField(default=0, null=True),
        ),
    ]