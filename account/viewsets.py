# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .serializers import RegisterSerializer
# from core.models import Employee
# from .permissions import IsPostOnly, AllowingGetAndUpdateForStaff
# from .models import User
# from .serializers import UserSerializer

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
