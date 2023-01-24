# from rest_framework import viewsets, permissions
# from .models import Employee
# from .serializers import EmployeeSerializer
# from .permissions import AllowingGetAndUpateForOwner

# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     permission_classes = [AllowingGetAndUpateForOwner]



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

