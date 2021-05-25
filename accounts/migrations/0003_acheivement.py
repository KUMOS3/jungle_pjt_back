# Generated by Django 3.2.3 on 2021-05-25 10:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_birth_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acheivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('acheived_users', models.ManyToManyField(blank=True, related_name='acheivements', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
