

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

# class FileLoadPDF(ViewSet):

#     renderer_classes = (PDFRenderer, )  # !important

#     def retrieve(self, request, pk):
#         queryset = FileModel.objects.filter(id=pk).get()

#         bytes = b64decode(queryset.file, validate=True)

#         pdf = BytesIO(bytes)  # Simulating File

#         return PDFResponse(
#             pdf.getvalue(),
#             file_name=queryset.uploader,
#             template_name=queryset.uploader,
#             status=status.HTTP_200_OK
#         )

# class FileLoadPDF(viewsets.ModelViewSet):
#     queryset = FileModel.objects.all()
#     serializer_class = FileSerilizer

#     @action(methods=['POST'], detail=True, url_path='upload-file')
#     def upload_file(self, request, pk=None):
#         """Upload an file """
#         f = self.get_object()
#         serializer = self.get_serializer(
#             f,
#             data=request.data
#         )

#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_200_OK
#             )

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )
