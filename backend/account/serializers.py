from rest_framework import serializers
from .models import AccountUser


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = "__all__"

    def create(self, validated_data):
        user = AccountUser.objects.create_user(**validated_data)
        return user
