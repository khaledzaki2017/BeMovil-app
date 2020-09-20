from rest_framework import serializers
from core.models import WizardForm, PhoneOTP, Partner
# from core.models import PhoneOTP, Step1FormModel, Step2FormModel, Step3FormModel, UserPictures, FileModel


class WizardFormSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(WizardFormSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = WizardForm
        # fields = ('id', 'firstname', 'lastname',
        #           'email',)
        fields = '__all__'
        read_only_fields = ('id',)


class PhoneOTPSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(PhoneOTPSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = PhoneOTP
        fields = '__all__'

        read_only_fields = ('id',)


# class Step1FormSerializer(serializers.ModelSerializer):
#     """Serializer for Step1Form objects"""

#     def __init__(self, *args, **kwargs):
#         many = kwargs.pop('many', True)
#         super(Step1FormSerializer, self).__init__(many=many, *args, **kwargs)

#     class Meta:
#         model = Step1FormModel
#         fields = ('id', 'firstname', 'lastname',
#                   'email', 'mobile_phone')
#         read_only_fields = ('id',)


# class Step2FormSerializer(serializers.ModelSerializer):
#     """Serializer for Step2FormModel objects"""

#     def __init__(self, *args, **kwargs):
#         many = kwargs.pop('many', True)
#         super(Step2FormSerializer, self).__init__(many=many, *args, **kwargs)

#     class Meta:
#         model = Step2FormModel
#         fields = ('id', 'address', 'city', 'valley')
#         read_only_fields = ('id',)


class FormImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images """

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(FormImageSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = WizardForm
        fields = ('id', 'id_image1', 'id_image2', 'client_image1',
                  'client_image2', 'client_image3')
        read_only_fields = ('id',)


class FileSerilizer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(FileSerilizer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = WizardForm
        fields = ('id', 'firstFile', 'secondFile', 'uploader')


class PartnerSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(PartnerSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Partner
        fields = '__all__'
class PartnerWizardSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(PartnerWizardSerializer, self).__init__(many=many, *args, **kwargs)


    # main= serializers.EmailField(source='wizardform.email')
    class Meta:
        model = Partner
        fields ='__all__'
