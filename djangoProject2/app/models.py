from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name

class Storage(models.Model):
    name = models.CharField(max_length=15)
    size = models.BigIntegerField(default=15 * 1024 ** 3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='app/static/files')
    category = models.CharField(max_length=2, choices=[("Ф", 'Фото'), ("В", 'Видео'), ("Д", 'Документы')])
    img = models.FileField(upload_to='app/static/fileimg', default='app/static/img/doc.png')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    file_size = models.BigIntegerField()
    size = models.ManyToManyField(to=Storage)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.size.exists():
            default_storage, created = Storage.objects.get_or_create(name='15', defaults={'size': 15 * 1024 ** 3})
            self.size.add(default_storage)
