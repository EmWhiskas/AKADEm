# Generated by Django 5.0.7 on 2024-07-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_file_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='img',
            field=models.FileField(default='/img/doc.png', upload_to='app/static/fileimg'),
        ),
    ]
