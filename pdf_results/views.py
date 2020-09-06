# from io import BytesIO
# from base64 import b64encode, b64decode
# from django.http.response import HttpResponseRedirect
# from rest_framework import status
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from drf_pdf.renderer import PDFRenderer
# from drf_pdf.response import PDFResponse
# from pdf_results.models import PDFfiles
# from pdf_results.serializers import PDFfilesList


# class PDFfilesView(ViewSet):

#     def list(self, request):
#         queryset = PDFfiles.objects.all()
#         serializer = PDFfilesList(queryset, many=True)

#         return Response(serializer.data)

#     def retrieve(self, request, pk):
#         return HttpResponseRedirect(redirect_to='/pdf/file/'+pk)

#     def create(self, request):
#         '''
#             Simple Custom Save Method
#         '''
#         title_file = request.data.get('title')
#         str_b64_file = request.data.get('file')

#         if not (title_file and str_b64_file):
#             return Response('Missing Data.')

#         i_PDFfiles = PDFfiles(
#             title=title_file,
#             file=b64encode(b64decode(str_b64_file))
#         ).save()

#         return PDFfiles('Data saved.')


# class PDFfilesLoadPDF(ViewSet):

#     renderer_classes = (PDFRenderer, )  # !important

#     def retrieve(self, request, pk):
#         queryset = PDFfiles.objects.filter(id=pk).get()

#         bytes = b64decode(queryset.file, validate=True)

#         pdf = BytesIO(bytes)  # Simulating File

#         return PDFResponse(
#             pdf.getvalue(),
#             file_name=queryset.title,
#             template_name=queryset.title,
#             status=status.HTTP_200_OK
#         )


# # from django.http import HttpResponse
# # from django.template.loader import get_template
# # from xhtml2pdf import pisa


# # def render_pdf_view(request):
# #     template_path = 'pdf_results/pdf.html'
# #     context = {'myvar': 'this is your template context'}
# #     # Create a Django response object, and specify content_type as pdf
# #     response = HttpResponse(content_type='application/pdf')
# #     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
# #     # find the template and render it.
# #     template = get_template(template_path)
# #     html = template.render(context)

# #     # create a pdf
# #     pisa_status = pisa.CreatePDF(
# #         html, dest=response,)
# #     # if error then show some funy view
# #     if pisa_status.err:
# #         return HttpResponse('We had some errors <pre>' + html + '</pre>')
# #     return response
import os

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http.response import HttpResponseRedirect
from drf_pdf.renderer import PDFRenderer
from drf_pdf.response import PDFResponse
from io import BytesIO
from base64 import b64encode, b64decode
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.parsers import MultiPartParser, FormParser
from .models import FileModel

from .serializers import FileSerilizer


from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)


def upload_handler(up_file, uploader):
    for f in up_file:
        dest = f'uploaded_files/{uploader}'
        if not os.path.exists(dest):
            os.makedirs(dest)
        default_storage.save(f'{dest}/{f}', ContentFile(f.read()))


class FileViewlist(APIView):

    def get(self, request):
        queryset = FileModel.objects.all()
        serializer = FileSerilizer(queryset, many=True)

        return Response(serializer.data)


class FileDetail(RetrieveAPIView):
    queryset = FileModel.objects.all()
    serializer_class = FileSerilizer


class FileLoadPDF(ViewSet):

    renderer_classes = (PDFRenderer, )  # !important

    def retrieve(self, request, pk):
        queryset = FileModel.objects.filter(id=pk).get()

        bytes = b64decode(queryset.file, validate=True)

        pdf = BytesIO(bytes)  # Simulating File

        return PDFResponse(
            pdf.getvalue(),
            file_name=queryset.uploader,
            template_name=queryset.uploader,
            status=status.HTTP_200_OK
        )


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        uploaded_files = request.FILES.getlist('file_name')
        uploader = dict(request.data)['uploader'][0]
        upload_handler(uploaded_files, uploader)
        file_serializer = FileSerilizer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
