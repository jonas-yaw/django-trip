# Generated by Django 3.0.7 on 2020-07-31 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]