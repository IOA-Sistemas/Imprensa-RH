from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Password"
    )
    
    class Meta:
        model = User 
        fields = ('id', 'username', 'email', 'is_staff', 'is_superuser', 'password', 'password_confirm')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
            is_staff = validated_data['is_staff'],
            is_superuser = validated_data['is_superuser']
        )
        password = validated_data['password']
        password_confirm = validated_data['password_confirm']
        
        if password != password_confirm:
            raise serializers.ValidationError({'password': 'The passwords doesnt match'})
        user.set_password(password)
        return user