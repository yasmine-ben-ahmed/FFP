# Generated by Django 4.1.7 on 2023-04-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0033_parcelle_namep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcelle',
            name='namep',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
