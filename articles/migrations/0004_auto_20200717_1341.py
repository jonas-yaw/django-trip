# Generated by Django 3.0.7 on 2020-07-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200717_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(auto_created=True, blank=True, max_length=255),
        ),
    ]
