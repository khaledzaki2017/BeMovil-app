from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
import random
from rest_framework.views import APIView
from core.models import PhoneOTP, Step1FormModel, Step2FormModel, Step3FormModel, UserPictures, FileModel
from multi_step_form import serializers
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

import os

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import viewsets, status
from rest_framework.decorators import action

from rest_framework.response import Response
from django.http.response import HttpResponseRedirect
from drf_pdf.renderer import PDFRenderer
from drf_pdf.response import PDFResponse
from io import BytesIO
from base64 import b64encode, b64decode
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.parsers import MultiPartParser, FormParser
# from .models import FileModel

from .serializers import FileSerilizer


from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)


# ********************FILE VIEWS******************************

def upload_handler(up_file, uploader):
    for f in up_file:
        dest = f'uploaded_files/{uploader}'
        if not os.path.exists(dest):
            os.makedirs(dest)
        default_storage.save(f'{dest}/{f}', ContentFile(f.read()))


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    queryset = FileModel.objects.all()
    serializer_class = FileSerilizer

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

    def get(self, request):
        queryset = FileModel.objects.all()
        serializer = FileSerilizer(queryset, many=True)

        return Response(serializer.data)


class FileDetail(RetrieveAPIView):
    queryset = FileModel.objects.all()
    serializer_class = FileSerilizer

# *************************FULL WIZARD DATA ********************************


class WizardFormViewSet(ObjectMultipleModelAPIViewSet):

    querylist = [
        {'queryset': Step1FormModel.objects.all(
        ), 'serializer_class': serializers.Step1FormSerializer},
        {'queryset': Step2FormModel.objects.all(
        ), 'serializer_class': serializers.Step2FormSerializer},
        {'queryset': Step3FormModel.objects.all(
        ), 'serializer_class': serializers.Step3FormSerializer},
        {'queryset': UserPictures.objects.all(
        ), 'serializer_class': serializers.FormImageSerializer},
        {'queryset': FileModel.objects.all(
        ), 'serializer_class': FileSerilizer}
    ]
# *********************************************************************


class Step1ViewSet(viewsets.ModelViewSet):
    queryset = Step1FormModel.objects.all()
    serializer_class = serializers.Step1FormSerializer


class Step2ViewSet(viewsets.ModelViewSet):
    queryset = Step2FormModel.objects.all()
    serializer_class = serializers.Step2FormSerializer


class Step3ViewSet(viewsets.ModelViewSet):
    queryset = Step3FormModel.objects.all()
    serializer_class = serializers.Step3FormSerializer

# ********************USER IMAGES VIEW**************


class UserPicturesViewSet(viewsets.ModelViewSet):
    queryset = UserPictures.objects.all()
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
