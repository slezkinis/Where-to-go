# Generated by Django 3.2.16 on 2023-01-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20230122_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to='media/', verbose_name='Картика'),
        ),
    ]
