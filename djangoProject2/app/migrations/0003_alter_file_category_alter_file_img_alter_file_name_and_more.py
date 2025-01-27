# Generated by Django 5.0.7 on 2024-07-11 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_file_category_file_user_delete_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='category',
            field=models.CharField(choices=[('Ф', 'Фото'), ('В', 'Видео'), ('Д', 'Документы')], max_length=2),
        ),
        migrations.AlterField(
            model_name='file',
            name='img',
            field=models.FileField(default='app/static/img/doc.png', upload_to='app/static/fileimg'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
