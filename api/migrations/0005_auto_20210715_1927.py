# Generated by Django 3.0 on 2021-07-15 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 7, 15, 19, 27, 7, 119924)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]