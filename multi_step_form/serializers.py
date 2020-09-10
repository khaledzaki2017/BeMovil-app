from rest_framework import serializers

from core.models import PhoneOTP, Step1FormModel, Step2FormModel, Step3FormModel, UserPictures, FileModel


# class WizardFormSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WizardFormModel
#         fields = '__all__'

#         read_only_fields = ('id',)


class PhoneOTPSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(PhoneOTPSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = PhoneOTP
        fields = '__all__'

        read_only_fields = ('id',)


class Step1FormSerializer(serializers.ModelSerializer):
    """Serializer for Step1Form objects"""

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(Step1FormSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Step1FormModel
        fields = ('id', 'firstname', 'lastname',
                  'email', 'mobile_phone')
        read_only_fields = ('id',)


class Step2FormSerializer(serializers.ModelSerializer):
    """Serializer for Step2FormModel objects"""

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(Step2FormSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Step2FormModel
        fields = ('id', 'address', 'city', 'valley')
        read_only_fields = ('id',)


class Step3FormSerializer(serializers.ModelSerializer):
    """Serializer for Step2FormModel objects"""

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(Step3FormSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Step3FormModel
        fields = ('id', 'number')
        read_only_fields = ('id',)


class FormImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images """

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(FormImageSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = UserPictures
        fields = ('id', 'image1', 'image2', 'image3')
        read_only_fields = ('id',)


class FileSerilizer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(FileSerilizer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = FileModel
        fields = ('id', 'firstFile', 'secondFile', 'uploader')
