from django.db import models
from django.conf import settings


class Filename(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='filenames')
    name = models.CharField(max_length=255)
    uploaded_file = models.ForeignKey('asd.UploadedFile', related_name='filenames')

    def __str__(self):
        return self.name


class UploadedFile(models.Model):
    file = models.FileField()
    checksum = models.CharField(max_length=32)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='uploaded_files', through=Filename)

    def __str__(self):
        return self.checksum
