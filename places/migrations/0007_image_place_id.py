# Generated by Django 3.2.16 on 2023-01-31 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_place_place_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='place_id',
            field=models.CharField(blank=True, max_length=200, verbose_name='ID места'),
        ),
    ]
