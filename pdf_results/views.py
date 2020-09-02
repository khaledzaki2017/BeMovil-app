# from django.shortcuts import render

from core.models import UserPictures
from wkhtmltopdf.views import PDFTemplateView
#from wkhtmltopdf.views import PDFTemplateResponse
# Create your views here.


class PDFResults(PDFTemplateView):

    def get_context_data(self, **kwargs):
        context_data = super(PDFResults, self).get_context_data(**kwargs)
        user_uuid = self.request.session.get('user_uuid')
        context_data.update({
            'first_name': self.request.session.get('first_name'),
            'last_name': self.request.session.get('last_name'),
            'local_address': self.request.session.get('local_address'),
            'permanent_address': self.request.session.get('permanent_address'),
            'user_images': UserPictures.objects.filter(user_uuid=user_uuid)
        })
        del self.request.session['first_name']
        del self.request.session['last_name']
        del self.request.session['local_address']
        del self.request.session['permanent_address']
        del self.request.session['user_uuid']
        return context_data
