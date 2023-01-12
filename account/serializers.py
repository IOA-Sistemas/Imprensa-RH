from rest_framework import serializers
from .models import User
from core.serializers import EmployeeSerializer
from core.models import Employee
# from rest_framework.serializers import NestedCreateSerializer

"""
    TODO: 
        - Create update and delete method
        - Retrieve Passoword
"""
class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Password"
    )
    
    class Meta:
        model = User 
        fields = ('id', 'cpf', 'email', 'is_staff', 'is_superuser', 'password', 'password_confirm')
        extra_kwargs = {'password': {'write_only': True}}
      
class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Password"
    )
    cpf = serializers.IntegerField()
    name = serializers.CharField()
    surname = serializers.CharField()
    # register_number = serializers.CharField()
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
    # id_role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    # id_association = serializers.PrimaryKeyRelatedField(queryset=EmploymentAssociation.objects.all())

    def create(self, validated_data):
        """
        TODO: Adicionar validacao para email
            - Verificar se já existe algum registro do email
            - Validacao formato do campo
        TODO: adicionar campo de is_staff, is_superuser
        """
        email = validated_data.pop('email')
        cpf = validated_data.pop('cpf')
        user_data = {
            'username': email,
            'email': email,
            'cpf': cpf,
            # is_staff = validated_data['is_staff'],
            # is_superuser = validated_data['is_superuser']
        }
        user = User.objects.create(**user_data)
        
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError({'password': 'The passwords doesnt match'})
        user.set_password(password)
        user.save()
        
        employee_data = {
            **validated_data,
            'user': user,
            'email': email
        }
        employee = Employee.objects.create(**employee_data)
        return employee, user