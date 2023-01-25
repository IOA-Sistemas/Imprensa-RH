from rest_framework import viewsets 
from account import serializers
from .models import Employees
from rest_framework import permissions
from account import permissions as custom_permission
# from rest_framework.response import Response
# from .permissions import IsPostOnly, AllowingGetAndUpdateForStaff

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = serializers.RegisterSerializer
    permission_classes = (custom_permission.IsPostOnly,)

class UpdateViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = serializers.UpdateEmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ChangePasswordViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    


# # Create your views here.
# class RegisterViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.none()
#     serializer_class = RegisterSerializer
#     permission_classes = [IsPostOnly]
    
#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # TODO
# # Create Userviewset allowing update and delete and set permissions
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowingGetAndUpdateForStaff]
