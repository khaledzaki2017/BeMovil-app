from django.contrib import admin
from .models import UserPictures
from pdf_results.models import FileModel as Files


admin.site.register(UserPictures)
# admin.site.register(PDFfiles)
admin.site.register(Files)
