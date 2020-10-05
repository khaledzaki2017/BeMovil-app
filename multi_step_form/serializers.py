from rest_framework import serializers
from core.models import WizardFormJuridica, WizardFormNatural, Partner, Email


class WizardFormNaturalSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(WizardFormNaturalSerializer, self).__init__(
            many=many, *args, **kwargs)

    class Meta:
        model = WizardFormNatural
        # fields = ('id', 'firstname', 'lastname',
        #           'email',)
        fields = '__all__'
        read_only_fields = ('id',)


class WizardFormJuridicaSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(WizardFormJuridicaSerializer, self).__init__(
            many=many, *args, **kwargs)

    class Meta:
        model = WizardFormJuridica
        # fields = ('id', 'firstname', 'lastname',
        #           'email',)
        fields = '__all__'
        read_only_fields = ('id',)


# class WizardNaturalUpdateSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         many = kwargs.pop('many', True)
#         super(WizardNaturalUpdateSerializer, self).__init__(
#             many=many, *args, **kwargs)

#     def update(self, instance, validated_data):

#         instance.status = validated_data["status"]

#         instance.save()

#         return instance

#     class Meta:
#         model = WizardFormNatural
#         # fields = ('id', 'firstname', 'lastname',
#         #           'email',)
#         fields = ['status']
#         read_only_fields = ('id',)


# class WizardJuridicaUpdateSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         many = kwargs.pop('many', True)
#         super(WizardJuridicaUpdateSerializer, self).__init__(
#             many=many, *args, **kwargs)

#     def update(self, instance, validated_data):

#         instance.status = validated_data["status"]

#         instance.save()

#         return instance

#     class Meta:
#         model = WizardFormJuridica
#         # fields = ('id', 'firstname', 'lastname',
#         #           'email',)
#         fields = ['status']
#         read_only_fields = ('id',)

# class ClientsDataSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         many = kwargs.pop('many', True)
#         super(ClientsDataSerializer, self).__init__(many=many, *args, **kwargs)

#     class Meta:
#         model = WizardForm
#         fields = ('id', 'firstname', 'lastname',
#                   'email', 'created_at')
#         read_only_fields = ('id',)


# class FormImageSerializer(serializers.ModelSerializer):
#     """Serializer for uploading images """

#     def __init__(self, *args, **kwargs):
#         many = kwargs.pop('many', True)
#         super(FormImageSerializer, self).__init__(many=many, *args, **kwargs)

#     class Meta:
#         model = WizardForm
#         fields = ('id_image1', 'id_image2', 'client_image1',
#                   'client_image2', 'client_image3')
#         # read_only_fields = ('id',)


# class FileSerilizer(serializers.ModelSerializer):

#     class Meta:
#         model = WizardForm
#         fields = ('firstFile', 'secondFile', 'uploader')


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
        super(PartnerWizardSerializer, self).__init__(
            many=many, *args, **kwargs)

    # main= serializers.EmailField(source='wizardform.email')

    class Meta:
        model = Partner
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = '__all__'
        read_only_fields = ('id',)
