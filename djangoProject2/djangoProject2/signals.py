from django.db.models.signals import pre_save
from django.dispatch import receiver
import os
from app.models import File

@receiver(pre_save, sender=File)
def update_file_size(sender, instance, **kwargs):
    if instance.file_path:
        instance.file_size = os.path.getsize(instance.file_path)