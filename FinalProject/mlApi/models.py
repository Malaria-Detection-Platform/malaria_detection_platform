from distutils.command.upload import upload
from django.db import models

# Create your models here.

class malaria(models.Model):
    cellImage = models.ImageField(upload_to='cellImages')
    result = models.CharField(max_length=200, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id)

    # def save(self, *args, **kwargs):
    #     return super().save(*args, **kwargs)