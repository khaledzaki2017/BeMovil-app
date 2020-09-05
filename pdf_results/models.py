# from datetime import datetime
# from django.db import models


# class PDFfiles(models.Model):

#     date = models.DateTimeField(default=datetime.now, null=False, blank=False)
#     title = models.CharField(max_length=255, null=False, blank=False)
#     file = models.BinaryField(null=False, blank=False)

#     def __str__(self):
#         return self.title
from django.db import models


class FileModel(models.Model):
    uploader = models.CharField(max_length=20)
    file_name = models.FileField(upload_to='documents')
    file = models.BinaryField(null=True, blank=False)

    def __str__(self):
        return self.uploader
