from rest_framework import viewsets, permissions
from .serializers import EmployeesSerializer
# from core import permissions as custom_permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
Employees = get_user_model()

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get']

# class ScholarityViewSet(viewsets.ModelViewSet):
#     queryset = Scholarity.objects.all()
#     serializer_class = ScholaritySerial
#     permission_classes = [permissions.IsAuthenticated]

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerial
#     permission_classes = [permissions.IsAuthenticated]

# class FunctionViewSet(viewsets.ModelViewSet):
#     queryset = Function.objects.all()
#     serializer_class = FunctionSerial
#     permission_classes = [permissions.IsAuthenticated]

# class DepartamentViewSet(viewsets.ModelViewSet):
#     queryset = Departament.objects.all()
#     serializer_class = DepartamentSerial
#     permission_classes = [permissions.IsAuthenticated]

# class BondViewSet(viewsets.ModelViewSet):
#     queryset = Bond.objects.all()
#     serializer_class = BondSerial
#     permission_classes = [permissions.IsAuthenticated]

# class AllocationViewSet(viewsets.ModelViewSet):
#     queryset = Allocation.objects.all()
#     serializer_class = AllocationSerial
#     permission_classes = [permissions.IsAuthenticated]

# class RelationAllocationFunctionViewSet(viewsets.ModelViewSet):
#     queryset = RelationAllocationFunction.objects.all()
#     serializer_class = RelationAllocationFunctionSerial
#     permission_classes = [permissions.IsAuthenticated]

