# Generated by Django 3.2.3 on 2021-05-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210523_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre_ids',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
