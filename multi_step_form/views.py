from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import mixins
from .sms import HablameSMS
from BeMovileApp.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMessage
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from django.core.files.storage import FileSystemStorage
import base64
from core.models import phoneModel
import pyotp
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import random
from core.models import WizardFormJuridica, WizardFormNatural, Partner, Email
from multi_step_form import serializers
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
import os
import django_filters
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from django_filters import rest_framework as filters
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt

# ******************Rest_Framework Imports******************************
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
import logging
logger = logging.getLogger('django')
# **************************************************************************************
# class TFilter(filters.FilterSet):

#     class Meta:
#         model = WizardForm
#         fields = {
#             '_type': ['icontains'],
#         }


class WizardFormNaturalListView(viewsets.ModelViewSet):
    # authentication_classes = (Authentication,)
    queryset = WizardFormNatural.objects.all()
    serializer_class = serializers.WizardFormNaturalSerializer
    # filterset_class = TFilter
    parser_classes = [MultiPartParser,
                      FileUploadParser, FormParser, JSONParser]

    def create(self, request):
        # files_list = request.FILES
        wizardData = request.data
        # firstUploaded_files = request.FILES.getlist('firstFile')
        # secondUploaded_files = request.FILES.getlist('secondFile')

        # uploader = dict(request.data)['uploader'][0]
        # upload_handler(firstUploaded_files, uploader)
        # upload_handler(secondUploaded_files, uploader)
        # serializer = self.serializer_class(
        #     data={"data": wizardData, "files": files_list})
        serializer = self.serializer_class(data=wizardData)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            wizard_data = serializer.data
            logger.info("created view of WizardFormNaturalListView")
            return Response(wizard_data,
                            status=status.HTTP_201_CREATED)
        else:
            logger.error('Something went wrong in WizardFormNaturalListView !')
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def wizardnatural_detail(request, pk):
    try:
        wizardnatural = WizardFormNatural.objects.get(pk=pk)
    except WizardFormNatural.DoesNotExist:
        logger.error('Something went wrong in wizardnatural_detail !')

        return JsonResponse({'message': 'The WizardFormNatural does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        WizardFormNatural_serializer = serializers.WizardFormNaturalSerializer(
            wizardnatural)
        return Response(WizardFormNatural_serializer.data)

    elif request.method == 'PUT':
        wizardnatural_data = JSONParser().parse(request)
        WizardFormNatural_serializer = serializers.WizardFormNaturalSerializer(
            wizardnatural, data=wizardnatural_data)
        if WizardFormNatural_serializer.is_valid():
            WizardFormNatural_serializer.save()
            return Response(WizardFormNatural_serializer.data)
        logger.error('Something went wrong in wizardnatural_detail !')
        return JsonResponse(WizardFormNatural_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        wizardnatural.delete()
        return JsonResponse({'message': 'wizardnatural was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class WizardFormJuridicaListView(viewsets.ModelViewSet):
    # authentication_classes = (Authentication,)
    queryset = WizardFormJuridica.objects.all()
    serializer_class = serializers.WizardFormJuridicaSerializer
    # filterset_class = TFilter
    parser_classes = [MultiPartParser,
                      FileUploadParser, FormParser, JSONParser]

    def create(self, request):
        # files_list = request.FILES
        wizardData = request.data
        # firstUploaded_files = request.FILES.getlist('firstFile')
        # secondUploaded_files = request.FILES.getlist('secondFile')

        # uploader = dict(request.data)['uploader'][0]
        # upload_handler(firstUploaded_files, uploader)
        # upload_handler(secondUploaded_files, uploader)

        # serializer = self.serializer_class(
        #     data={"data": wizardData, "files": files_list})
        serializer = self.serializer_class(data=wizardData)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            wizard_data = serializer.data

            return Response(wizard_data,
                            status=status.HTTP_201_CREATED)
        else:
            logger.error('Something went wrong in WizardFormJuridicaListView')
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


# def img_handler(data):
#     format, imgstr = data.split(';base64,')
#     ext = format.split('/')[-1]
#     print('hereeeeeeeeeeeeeeeeeeeeee')
#     # You can save this as file instance.
#     data_f = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
#     return data_f

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def wizardjuridica_detail(request, pk):
    try:
        wizardjuridica = WizardFormJuridica.objects.get(pk=pk)
    except WizardFormJuridica.DoesNotExist:
        return JsonResponse({'message': 'The WizardFormJuridica does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        WizardFormJuridica_serializer = serializers.WizardFormJuridicaSerializer(
            wizardjuridica)
        return Response(WizardFormJuridica_serializer.data)

    elif request.method == 'PUT':
        wizardjuridica_data = JSONParser().parse(request)
        WizardFormJuridica_serializer = serializers.WizardFormJuridicaSerializer(
            wizardjuridica, data=wizardjuridica_data)
        if WizardFormJuridica_serializer.is_valid():
            WizardFormJuridica_serializer.save()
            return Response(WizardFormJuridica_serializer.data)
        return JsonResponse(WizardFormJuridica_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        wizardjuridica.delete()
        return JsonResponse({'message': 'wizardjuridica was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# def upload_handler(up_file, uploader):
#     for f in up_file:
#         print(f)
#         dest = f'uploaded_files/{uploader}'
#         # current_site = get_current_site(request).domain

#         if not os.path.exists(dest):
#             os.makedirs(dest)

#         default_storage.save(
#             f'{dest}/{f}', ContentFile(f.read()))


class EmailCheck(generics.GenericAPIView):

    queryset = Email.objects.all()
    serializer_class = serializers.EmailSerializer

    def post(self, request):
        if (request):
            client_name = request.POST.get('firstname', '')
            mail_id = request.POST.get('email', '')
            email = EmailMessage("[Be-Movil]Check Your Contract Informations", "Hello, "+client_name +
                                 "Please, check your data in the file attached below\n", EMAIL_HOST_USER, [mail_id])
            email.content_subtype = 'html'

            file = request.FILES['final_pdf']
            email.attach(file.name, file.read(), file.content_type)

            email.send()
            return Response("Email sent successfully ",
                            status=status.HTTP_201_CREATED)
        else:
            return Response("try again!, something wrong",
                            status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
        # wizardData = request.data
        # fulldata = self.request.data

        # serializer = self.serializer_class(data=fulldata)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        # # wizard_data = serializer.data
        # if(fulldata):
            # print(fulldata)
            # client_email = fulldata['email']
            # print(client_email)
            # client_name = fulldata['firstname']
            # print(client_name)
            # current_site = get_current_site(request).domain
            # # final_pdf = self.request.FILES['final_pdf'].file.name
            # # content = final_pdf.read()  # For small files

            # # relativeLink = reverse('multi_step_form:email-check')
            # # absurl = 'http://' + current_site + content
            # email_body = "Hello, "+client_name + \
            #     " check yor data in the file below\n"
            # print(email_body)
            # data = {'email_body': email_body, 'to_email': [client_email],
            #         'email_subject': 'check your data'}
            # print(data)
            # Util.send_email(data)


class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


class getPhoneNumberRegistered(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        try:
            # if Mobile already exists the take this else create New One
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                Mobile=phone,
            )
            Mobile = phoneModel.objects.get(
                Mobile=phone)
        Mobile.counter += 1  # Update Counter At every Call
        Mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(
            phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(Mobile.counter))
        # need IP Auth
        HablameSMS(
            f'{phone}', f'This is your OTP CODE{OTP.at(Mobile.counter)}').recharge()
        # just for testing
        return Response({"OTP": OTP.at(Mobile.counter)}, status=200)

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(
            phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong", status=400)


# *************************FULL WIZARD DATA ********************************


class WizardFormViewSet(ObjectMultipleModelAPIViewSet):

    querylist = [
        {'queryset': WizardFormNatural.objects.all(
        ), 'serializer_class': serializers.WizardFormNaturalSerializer},
        {'queryset': WizardFormJuridica.objects.all(
        ), 'serializer_class': serializers.WizardFormJuridicaSerializer},
        {'queryset': Partner.objects.all(
        ), 'serializer_class': serializers.PartnerSerializer}
    ]

# ***************************** Partner View ****************************************


class PartnerMainWizardFilter(django_filters.FilterSet):
    partner = django_filters.Filter(field_name="WizardForm__email")

    class Meta:
        model = Partner
        fields = ['main']


class PartnerMainWizardListAPIView(ListAPIView):

    queryset = Partner.objects.all()
    serializer_class = serializers.PartnerWizardSerializer
    filter_class = PartnerMainWizardFilter


# class PartnerView(APIView):
#     queryset = Partner.objects.all()
#     serializer_class = serializers.PartnerSerializer

#     def post(self, request, *args, **kwargs):
#         print(request.data)
#         PartnerData = request.data
#         serializer = self.serializer_class(data=PartnerData)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             # partner_data = serializer.data.filter(
#             #     email=self.request.data.main)
#             return Response(serializer.data,
#                             status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, *args, **kwargs):
#         queryset = Partner.objects.all()
#         serializer_class = serializers.PartnerSerializer()
#         return Response(serializer_class.data)


class PartnerView(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet create and list partner
    """
    queryset = Partner.objects.all()
    serializer_class = serializers.PartnerSerializer
    # search_fields = ('name','author')

    def create(self, request, *args, **kwargs):

        is_many = isinstance(request.data, list)
        if not is_many:
            return super(PartnerView, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# ********************************************************************************************************
@api_view(['POST'])
def generate_token(request):
    if request.method == 'POST':
        serializer = serializers.AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
