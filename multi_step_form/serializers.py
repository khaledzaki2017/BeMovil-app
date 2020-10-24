from rest_framework import serializers
from core.models import WizardFormJuridica, WizardFormNatural, Partner, Email, phoneModel, AuthToken
# from drf_extra_fields.fields import Base64ImageField


class WizardFormNaturalSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(WizardFormNaturalSerializer, self).__init__(
            many=many, *args, **kwargs)

    firstFile = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = WizardFormNatural
        # fields = ('id', 'firstname', 'lastname',
        #           'email',)
        fields = '__all__'


class WizardFormJuridicaSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(WizardFormJuridicaSerializer, self).__init__(
            many=many, *args, **kwargs)
    # id_image1 = Base64ImageField()
    firstFile = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = WizardFormJuridica
        # fields = ('id', 'firstname', 'lastname',
        #           'email',)
        fields = '__all__'

        # def create(self, validated_data):
        #     id_image1 = validated_data.pop('id_image1')
        #     # data = validated_data.pop('data')
        #     return WizardFormJuridica.objects.create(id_image1=id_image1)


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


class AuthTokenSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=phoneModel.objects.all(), write_only=True)

    class Meta:
        model = AuthToken
        fields = ('key', 'created', 'id')
        read_only_fields = ('key', 'created')

    def create(self, validated_data):

        validated_data.pop('id')

        return super().create(validated_data)
