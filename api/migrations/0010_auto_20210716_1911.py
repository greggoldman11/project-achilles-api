# Generated by Django 3.0 on 2021-07-16 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210716_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]