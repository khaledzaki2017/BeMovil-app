from django.contrib import admin
from .models import WizardFormModel as WizardForm
from pdf_results.models import FileModel as Files


admin.site.register(WizardForm)
# admin.site.register(PDFfiles)
admin.site.register(Files)
