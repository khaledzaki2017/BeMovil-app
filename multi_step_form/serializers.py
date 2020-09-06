from rest_framework import serializers

from core.models import WizardFormModel
# ,Step1FormModel, Step2FormModel, Step3FormModel, UserPictures


class WizardFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = WizardFormModel
        fields = '__all__'

        read_only_fields = ('id',)


# class Step1FormSerializer(serializers.ModelSerializer):
#     """Serializer for Step1Form objects"""

#     class Meta:
#         model = Step1FormModel
#         fields = ('id', 'firstname', 'lastname', 'address',
#                   'email', 'city', 'mobile_phone')
#         read_only_fields = ('id',)


# class Step2FormSerializer(serializers.ModelSerializer):
#     """Serializer for Step2FormModel objects"""

#     class Meta:
#         model = Step2FormModel
#         fields = ('id', 'address', 'city', 'valley')
#         read_only_fields = ('id',)


# class Step3FormSerializer(serializers.ModelSerializer):
#     """Serializer for Step2FormModel objects"""

#     class Meta:
#         model = Step3FormModel
#         fields = ('id', 'number')
#         read_only_fields = ('id',)


# # class FormsDetailSerializer(RecipeSerializer):
# #     """Serialize a forms detail"""
# #     step1 = Step2FormSerializer(many=True, read_only=True)
# #     step2 = Step2FormSerializer(many=True, read_only=True)
# #     step3 = Step2FormSerializer(many=True, read_only=True)
# #     uploaded = FormImageSerializer(many=True, read_only=True)


# class FormImageSerializer(serializers.ModelSerializer):
#     """Serializer for uploading images """

#     class Meta:
#         model = UserPictures
#         fields = ('id', 'image1', 'image2', 'image3')
#         read_only_fields = ('id',)
