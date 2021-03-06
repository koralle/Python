# Generated by Django 3.0 on 2019-12-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='タスクID')),
                ('deadline', models.DateTimeField(verbose_name='期限')),
                ('title', models.TextField(max_length=255, verbose_name='タスク名')),
                ('content', models.TextField(blank=True, max_length=255, verbose_name='タスク詳細')),
            ],
        ),
    ]
