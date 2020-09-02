from django.urls import path
from pdf_results.views import PDFResults

app_name = 'pdf_results'
urlpatterns = [
    path('', PDFResults.as_view(template_name='pdf_results/pdf.html',
                                filename='user_details.pdf'), name='pdf'),
]
