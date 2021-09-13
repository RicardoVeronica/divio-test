from django.db import models


class UploadedFile(models.Model):
    name = models.CharField(max_length=100, default='file')
    file = models.FileField()

    def __str__(self):
        return self.name
