# Generated by Django 3.0 on 2019-12-22 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0002_auto_20191222_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardmodel',
            old_name='red',
            new_name='read',
        ),
    ]
