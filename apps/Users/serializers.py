from rest_framework import serializers
from .models import User, TypeUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'photo', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user_type = TypeUser.objects.get(name__iexact='Comum')
        validated_data['user_type'] = user_type
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'photo', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['is_staff'] = True
        validated_data['is_superuser'] = True
        validated_data['is_active'] = True
        
        user_type = TypeUser.objects.get(name__iexact='Admin')
        validated_data['user_type'] = user_type
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user