# Generated by Django 5.0.7 on 2024-07-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_file_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='name',
            field=models.CharField(default=15, max_length=15),
            preserve_default=False,
        ),
    ]
