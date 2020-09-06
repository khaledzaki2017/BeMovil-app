from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status

from core.models import WizardFormModel
#  Step1FormModel, Step2FormModel, Step3FormModel, UserPictures
from multi_step_form import serializers


class WizardFormViewSet(viewsets.ModelViewSet):
    queryset = WizardFormModel.objects.all()
    serializer_class = serializers.WizardFormSerializer

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

# #    def getInitialdata(self, request, *args, **kwargs):
# #        sk = request.GET.get('sk', '')
# #        data = request.get_serializer
# #        if data:
# #           s = SessionStore(session_key=sk)
# #           s.delete()
# #             return Response({'result': data})
# #        return Response({'result': 'no data'})


# class Step2ViewSet(viewsets.ModelViewSet):
#     queryset = Step2FormModel.objects.all()
#     serializer_class = serializers.Step2FormSerializer


# class Step3ViewSet(viewsets.ModelViewSet):
#     queryset = Step3FormModel.objects.all()
#     serializer_class = serializers.Step3FormSerializer


# class UserPicturesViewSet(viewsets.ModelViewSet):
#     queryset = UserPictures.objects.all()
#     serializer_class = serializers.FormImageSerializer

#     @action(methods=['POST'], detail=True, url_path='upload-image')
#     def upload_image(self, request, pk=None):
#         """Upload an image """
#         form = self.get_object()
#         serializer = self.get_serializer(
#             form,
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

# class ValidatePhoneSendOTP(APIView):


#     def post(self, request, *args, **kwargs):
#         phone_num = request.data.get('phone')
#         if phone_num:
#             phone = str(phone_num)
#             user=User.objects.filter(phon)
