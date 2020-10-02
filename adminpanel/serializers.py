from rest_framework import serializers
from core.models import User, UserProfile
from drf_writable_nested.serializers import WritableNestedModelSerializer


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)
    # profile = serializers.HyperlinkedIdentityField(
    #     view_name='user-detail',
    #     many=True,
    #     read_only=True,
    #     lookup_field='email')
    # extra_kwargs = {'url': {'view_name': 'adminpanel_users:user-detail'}}

    class Meta:
        model = User
        fields = ('email', 'first_name',
                  'last_name', 'password', "profile")
        extra_kwargs = {'password': {'write_only': True}}
        # lookup_field = 'user__username'

        def create(self, validated_data):
            # profile_data = validated_data.pop('profile')
            password = validated_data.pop('password')
            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.save()
            # for o in profile_data:
            #     UserProfile.objects.create(user=user, **profile_data)
            return user

        def update(self, instance, validated_data):
            # profile_data = validated_data.pop('profile')
            # profile = instance.profile

            instance.email = validated_data.get('email', instance.email)
            instance.save()

            # profile.title = profile_data.get('title', profile.title)
            # profile.dob = profile_data.get('dob', profile.dob)

            # profile.photo = profile_data.get('photo', profile.photo)
            # profile.save()

            return instance
