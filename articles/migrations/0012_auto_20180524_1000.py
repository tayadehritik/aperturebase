# Generated by Django 2.0.5 on 2018-05-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_cat_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='imgs0',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='cat',
            name='imgs1',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='cat',
            name='imgs2',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='cat',
            name='imgs3',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='cat',
            name='imgs4',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='cat',
            name='imgs5',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]