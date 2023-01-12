# from rest_framework import viewsets, permissions
# from .models import Employee
# from .serializers import EmployeeSerializer
# from account.models import User
# from account.serializers import UserSerializer
# from rest_framework.response import Response
# from rest_framework import status

# class SignUpViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.none()
#     serializer_class = UserSerializer
    
#     def create(self, request, *args, **kwargs):
#         try:
#             user_serializer = UserSerializer(data = request.data)
#             user_serializer.is_valid(raise_exception=True)
#             user = user_serializer.save()
            
#             employee_data = request.data.pop('employee')
#             employee_data['user'] = user.id
#             employee_serializer = EmployeeSerializer(data = employee_data)
#             employee_serializer.is_valid(raise_exception=True)
#             employee_serializer.save()
            
#             return Response({'message': 'User created sucessfully'}, status=status.HTTP_201_CREATED)
#         except:
            
#             return Response({'message': 'Sorry something happened and we couldnt create the user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerial
#     permission_classes = [permissions.IsAuthenticated]

# class AllocationViewSet(viewsets.ModelViewSet):
#     queryset = Allocation.objects.all()
#     serializer_class = AllocationSerial
#     permission_classes = [permissions.IsAuthenticated]

# class RelationAllocationFunctionViewSet(viewsets.ModelViewSet):
#     queryset = RelationAllocationFunction.objects.all()
#     serializer_class = RelationAllocationFunctionSerial
#     permission_classes = [permissions.IsAuthenticated]

