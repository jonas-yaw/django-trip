# Generated by Django 3.0.7 on 2020-07-17 12:38

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200717_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(auto_created=True, default=articles.models.Article.author_default, max_length=144),
        ),
    ]
