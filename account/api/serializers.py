from rest_framework import serializers
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
        )

    def validate_password(self, value):
        user = self.context['request'].user
        password_validation.validate_password(value, user)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user