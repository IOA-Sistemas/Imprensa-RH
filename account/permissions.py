from rest_framework import permissions
from django.http import HttpResponse
from rest_framework import serializers

class IsPostOnly(permissions.BasePermission):
    """
    Custom permission to only allow `POST` requests.
    """
    def has_permission(self, request, view):
        if request.method != 'POST':
            raise serializers.ValidationError("This endpoint only allows POST requests.")
        return True