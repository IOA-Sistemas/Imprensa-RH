from rest_framework import permissions
from rest_framework import serializers

class IsGetOnly(permissions.BasePermission):
    """
    Custom permission to only allow `POST` requests.
    """
    def has_permission(self, request, view):
        if request.method != 'GET' and request.user.is_authenticated:
            raise serializers.ValidationError("This endpoint only allows POST requests.")
        return True


# class AllowingGetAndUpateForOwner(permissions.BasePermission):
#     """
#         Allowing Get for authenticated users and update for objects owenrs and staff
#     """
#     allowed_methods = ['GET', 'PUT', 'PATCH']
#     allowed_actions = ['retrieve', 'update', 'partial_update', 'destroy']
    
#     def has_permission(self, request, view):
#         if request.method in self.allowed_methods and request.user.is_authenticated:
#             return True
#         elif request.method == 'DELETE' and request.user.is_staff:
#             return True
#         else: 
#             return False

#     def has_object_permission(self, request, view, obj):
#         if view.action in self.allowed_actions:
#             if obj.id == request.user.id or request.user.is_staff:
#                 return True
#         else:
#             return False


       
       



