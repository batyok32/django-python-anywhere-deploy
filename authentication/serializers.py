from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


# For Sign up and list
class UserCreateeSerializer(UserCreateSerializer):
    city_display = serializers.CharField(
        source='get_city_display'
    )
    profile_social = serializers.SerializerMethodField()
    profile_avatar = serializers.SerializerMethodField()

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'phone_number',
                  'password', 'address', 'city', 'city_display', 'profile_social', 'profile_avatar')
        read_only_fields = ['city_display', 'profile_social', 'profile_avatar']

    def get_profile_social(self, obj):
        return self.context['request'].build_absolute_uri( obj.profile_social.url)
    
    def get_profile_avatar(self, obj):
        return self.context['request'].build_absolute_uri( obj.profile_avatar.url)
    

# Detail User
class UserDetailSerializer(serializers.ModelSerializer):
    city_display = serializers.CharField(
        source='get_city_display'
    )
    profile_social = serializers.SerializerMethodField()
    profile_avatar = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "phone_number","profile_img", "profile_social",'profile_avatar', "address","city","city_display","is_active", "is_staff", "date_joined", "email")
        read_only_fields = ['id', 'is_active', "is_staff", "date_joined", 'city_display', "profile_social", 'profile_avatar']
    
    def get_profile_social(self, obj):
        return self.context['request'].build_absolute_uri( obj.profile_social.url)
    
    def get_profile_avatar(self, obj):
        return self.context['request'].build_absolute_uri( obj.profile_avatar.url)