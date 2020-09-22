from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
import random
from rest_framework.views import APIView
from core.models import PhoneOTP, WizardForm, Partner
from multi_step_form import serializers
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
from .serializers import FileSerilizer, PartnerSerializer,PartnerWizardSerializer
import os
import django_filters
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import viewsets, status
from rest_framework.decorators import action

from rest_framework.response import Response
from django.http.response import HttpResponseRedirect
# from drf_pdf.renderer import PDFRenderer
# from drf_pdf.response import PDFResponse
from io import BytesIO
from base64 import b64encode, b64decode
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.parsers import MultiPartParser, FormParser
# from .models import FileModel
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser

from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)
from rest_framework.authentication import TokenAuthentication

from django_filters import rest_framework as filters

# class JSONWebTokenAuthentication(TokenAuthentication):
#     def authenticate_credentials(self, jwtToken):
#         try:
#             payload = jwt.decode(jwtToken, secret_key, verify=True)
#             # user = User.objects.get(username='root')
#             user = AnonymousUser()
#         except (jwt.DecodeError, User.DoesNotExist):
#             raise exceptions.AuthenticationFailed('Invalid token)
#         except jwt.ExpiredSignatureError:
#             raise exceptions.AuthenticationFailed('Token has expired')
#         return (user, payload)


from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token


class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth = authentication.get_authorization_header(request)
        print("here", auth)
        if not auth or auth[0].lower() != b'token':
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _(
                'Invalid token header. Credentials string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = Token.objects.get(token=auth[1])
            print(token.key)

        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such token')

        return (AnonymousUser(), token)


# ********************FILE VIEWS******************************

def upload_handler(up_file, uploader):
    for f in up_file:
        dest = f'uploaded_files/{uploader}'
        if not os.path.exists(dest):
            os.makedirs(dest)
        default_storage.save(f'{dest}/{f}', ContentFile(f.read()))


class FileView(APIView):
    authentication_classes = (Authentication,)
    parser_classes = (MultiPartParser, FormParser,)
    queryset = WizardForm.objects.values("firstFile", "secondFile", "uploader")
    serializer_class = serializers.FileSerilizer

    def post(self, request, *args, **kwargs):
        firstUploaded_files = request.FILES.getlist('firstFile')
        secondUploaded_files = request.FILES.getlist('secondFile')

        uploader = dict(request.data)['uploader'][0]
        upload_handler(firstUploaded_files, uploader)
        upload_handler(secondUploaded_files, uploader)
        file_serializer = FileSerilizer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileViewlist(APIView):
    authentication_classes = (Authentication,)

    def get(self, request):
        queryset = WizardForm.objects.values("firstFile", "secondFile")
        serializer = serializers.FileSerilizer(queryset, many=True)

        return Response(serializer.data)


class FileDetail(RetrieveAPIView):
    authentication_classes = (Authentication,)

    def get(self, request, pk=None):
        queryset = WizardForm.objects.values("firstFile", "secondFile")
        serializer_class = serializers.FileSerilizer()
        return Response(serializer_class.data)

# *************************FULL WIZARD DATA ********************************


class WizardFormViewSet(ObjectMultipleModelAPIViewSet):

    querylist = [
        {'queryset': WizardForm.objects.all(
        ), 'serializer_class': serializers.WizardFormSerializer},
        {'queryset': PhoneOTP.objects.all(
        ), 'serializer_class': serializers.PhoneOTPSerializer},
        {'queryset':Partner.objects.all(),'serializer_class':PartnerSerializer}
    ]

# *********************************************************************


class TFilter(filters.FilterSet):

    class Meta:
        model = WizardForm
        fields = {
            '_type': ['icontains'],
        }


class WizardFormListView(viewsets.ModelViewSet):
    # authentication_classes = (Authentication,)
    queryset = WizardForm.objects.all()
    serializer_class = serializers.WizardFormSerializer
    filterset_class = TFilter



    def create(self, request):
        wizardData = request.data
        serializer = self.serializer_class(data=wizardData)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            wizard_data = serializer.data
            # print(wizard_data)
            # client_email = wizard_data['email']
            # print(client_email)
            # client_name = wizard_data['firstname']
            # print(client_name)
            # current_site = get_current_site(request).domain
            #
            # relativeLink = reverse('multi_step_form:email-check')
            # absurl = 'http://' + current_site + relativeLink
            # email_body = "Hello,"+client_name + "check yor data in the file below\n" + absurl
            # print(email_body)
            # data = {'email_body': email_body, 'to_email': [client_email],
            #         'email_subject': 'check your data'}
            # print(data)
            # Util.send_email(data)

            return Response(wizard_data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class EmailCheck(generics.GenericAPIView):
    def get(self):
        pass




class PartnerMainWizardFilter(django_filters.FilterSet):
    partner = django_filters.Filter(field_name="WizardForm__email")

    class Meta:
        model = Partner
        fields = ['main']


# class PartnerMainWizardListAPIView(ListAPIView):
#
#     serializer_class = PartnerWizardSerializer
#
#     def get_queryset(self):
#         queryset = Partner.objects.all()
#         main = self.request.query_params.get("main", None)
#         print(main)
#         if main is not None:
#             queryset = queryset.filter(WizardForm__icontains=main)
#         return queryset
class PartnerMainWizardListAPIView(ListAPIView):

    queryset = Partner.objects.all()
    serializer_class = PartnerWizardSerializer
    filter_class = PartnerMainWizardFilter

class PartnerView(APIView):
    queryset = Partner.objects.all()
    serializer_class = serializers.PartnerSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        PartnerData = request.data
        serializer = self.serializer_class(data=PartnerData)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # partner_data = serializer.data.filter(
            #     email=self.request.data.main)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


# class Step2ViewSet(viewsets.ModelViewSet):
#     queryset = Step2FormModel.objects.all()
#     serializer_class = serializers.Step2FormSerializer


# class Step3ViewSet(viewsets.ModelViewSet):
#     queryset = Step3FormModel.objects.all()
#     serializer_class = serializers.Step3FormSerializer

# ********************USER IMAGES VIEW**************


class UserPicturesViewSet(viewsets.ModelViewSet):
    queryset = WizardForm.objects.values('id_image1', 'id_image2', 'client_image1',
                                         'client_image2', 'client_image3')
    serializer_class = serializers.FormImageSerializer

    @action(methods=['POST'], detail=True)
    def upload_image(self, request, pk=None):
        """Upload an image """
        form = self.get_object()
        serializer = self.get_serializer(
            form,
            data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# class Step1ViewSet(viewsets.ModelViewSet):
#     queryset = Step1FormModel.objects.all()
#     serializer_class = serializers.Step1FormSerializer

#    def getInitialdata(self, request, *args, **kwargs):
#        sk = request.GET.get('sk', '')
#        data = request.get_serializer
#        if data:
#           s = SessionStore(session_key=sk)
#           s.delete()
#             return Response({'result': data})
#        return Response({'result': 'no data'})


# **********************OTP VALIDATION*******************************

class ValidatePhoneSendOTP(APIView):
    queryset = PhoneOTP.objects.all()
    serializer_class = serializers.PhoneOTPSerializer

    def post(self, request, *args, **kwargs):
        phone_num = request.data.get('phone')
        if phone_num:
            phone = str(phone_num)
            # user = User.objects.filter(phone__iexact=phone)
            # if user.exists():
            #     return Response({'status': False, 'detail': 'phone number already exist'})
            # else:
            key = send_otp(phone)
            if key:
                old = PhoneOTP.objects.filter(phone__iexact=phone)
                if old.exists():
                    old = old.first()
                    count = old.count
                    if count > 10:
                        return Response({'status': False, 'detail': 'sending OTP limit exceeded'})
                    else:
                        old.count = count + 1
                        old.save()
                        return Response({'status': True, 'detail': 'OTP sended successfully'})

                else:

                    PhoneOTP.objects.create(
                        phone=phone,
                        otp=key
                    )
                    return Response({'status': True, 'detail': 'OTP sended successfully'})

            else:
                return Response({'status': False, 'detail': 'sending otp has error'})

        else:
            return Response({'status': False, 'detail': 'phone number is not givin in the request'})


def send_otp(phone):
    if phone:
        key = random.randint(999, 9999)
        print(key)
        return key
    else:
        return False
