# Generated by Django 3.2.16 on 2023-01-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='place_id',
        ),
        migrations.AddField(
            model_name='place',
            name='description_long',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='place',
            name='description_short',
            field=models.CharField(blank=True, max_length=200, verbose_name='Короткое описание'),
        ),
    ]
