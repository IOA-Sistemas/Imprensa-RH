from rest_framework import serializers
from .models import Employees
from core.models import EmploymentAssociation, Role
import re
from django.db.models import Q


class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()
    cpf = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label="Password")
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True, label="Password Confirm")
    name = serializers.CharField()
    birth_date = serializers.DateField()
    gender = serializers.CharField()
    admission_date = serializers.DateField()
    address = serializers.CharField()
    neighborhood = serializers.CharField()
    city = serializers.CharField()
    post_code = serializers.CharField()
    state = serializers.CharField()
    phone = serializers.IntegerField()
    email = serializers.EmailField()
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), source='id_role')
    association = serializers.PrimaryKeyRelatedField(queryset=EmploymentAssociation.objects.all(), source='id_association')

    def create(self, validated_data):
        email = self.validated_data['email']
        cpf = self.validated_data['cpf']
        
        # validations
        email_validation = re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email.lower())
        cpf_validation = re.match(
            '\d{3}\.\d{3}\.\d{3}\-\d{2}',
            str(cpf)
        )
        if not email_validation:
            raise serializers.ValidationError('Invalid email format')
            return
        if not cpf_validation: 
            raise serializers.ValidationError('Invalid cpf')
            return
        if Employees.objects.filter(Q(email=email) | Q(cpf=cpf)).exists():
            raise serializers.ValidationError({'email': 'Email or CPF already exists'})
            return
        
        password = self.validated_data['password']
        password_confirm = validated_data.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError({'password': 'The passwords doesnt match'})
        
        employee = Employees.objects.create(**validated_data)
        employee.set_password(password)
        employee.save()
        return employee


class UpdateEmployeeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    address = serializers.CharField()
    neighborhood = serializers.CharField()
    city = serializers.CharField()
    post_code = serializers.CharField()
    state = serializers.CharField()
    phone = serializers.IntegerField()
    email = serializers.EmailField()
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), source='id_role')
    association = serializers.PrimaryKeyRelatedField(queryset=EmploymentAssociation.objects.all(), source='id_association')
    
    def update(self, instance, validated_data):
        user = self.context['request'].user
        email = self.validated_data['email']
        
        # validations
        if user.pk != instance.pk or user.is_staff:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
            return 
        email_validation = re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email.lower())
        if not email_validation:
            raise serializers.ValidationError('Invalid email format')
            return 
        if Employees.objects.exclude(pk=user.pk).filter(email=email).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
            return
        
        instance.email = validated_data['email']
        instance.name = validated_data['name']
        instance.adress = validated_data['adress']
        instance.neighborhood = validated_data['neighborhood']
        instance.city = validated_data['city']
        instance.post_code = validated_data['post_code']
        instance.state = validated_data['state']
        instance.phone = validated_data['phone']
        instance.role = validated_data['role']
        instance.association = validated_data['association']
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label="Old Password")
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label="Password")
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True, label="Password Confirm")
    
    def update(self, instance, validated_data):
        user = self.context['request'].user
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']
        old_password = self.validated_data['old_password']
        
        if password != password_confirm:
            raise serializers.ValidationError('Password and Passowrd confirm did not match')
            return
        if not user.check_password(old_password):
            raise serializers.ValidationError('Old password is incorrect')
            return
        
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
        


       
        
