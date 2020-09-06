# from rest_framework import serializers
# from pdf_results.models import PDFfiles


# class PDFfilesList(serializers.ModelSerializer):

#     class Meta:
#         model = PDFfiles
#         fields = ['id', 'date', 'title']
from rest_framework import serializers
from .models import FileModel


class FileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ('id', 'firstFile', 'secondFile', 'uploader')
