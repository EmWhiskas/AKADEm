# Generated by Django 5.0.7 on 2024-07-11 03:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='category',
            field=models.CharField(blank=True, choices=[('Ф', 'Фото'), ('В', 'Видео'), ('Д', 'Документы')], max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]