from rest_framework import serializers
from .models import CustomUser
from projects.models import ProjectCategory


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        new_user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user