# Generated by Django 3.0 on 2021-07-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210716_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
