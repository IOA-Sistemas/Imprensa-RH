from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id', 'user','name', 'surname', 'register_number', 'birth_date', 'gender', 'admission_date',
            'address', 'neighborhood', 'city', 'post_code', 'state', 'phone', 'email', 'id_role',
            'id_association'
        )

# class ScholaritySerial(serializers.ModelSerializer):
#     class Meta:
#         model = Scholarity
#         fields = ('__all__')

# class PostSerial(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('__all__')

# class FunctionSerial(serializers.ModelSerializer):
#     class Meta:
#         model = Function
#         fields = ('__all__')

# class DepartamentSerial(serializers.ModelSerializer):
#     class Meta:
#         model = Departament
#         fields = ('__all__')

# class BondSerial(serializers.ModelSerializer):
#     class Meta:
#         model = Bond
#         fields = ('__all__')

# class AllocationSerial(serializers.ModelSerializer):
#     class Meta:
#         model = Allocation
#         fields = ('__all__')

# class RelationAllocationFunctionSerial(serializers.ModelSerializer):
#     class Meta:
#         model = RelationAllocationFunction
#         fields = ('__all__')