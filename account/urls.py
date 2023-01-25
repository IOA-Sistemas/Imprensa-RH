from rest_framework.routers import DefaultRouter
from account import viewsets

router = DefaultRouter()
router.register(r'register', viewsets.RegisterViewSet, basename='register')
router.register(r'update<int:pk>', viewsets.UpdateViewSet, basename='update')
router.register(r'change_password', viewsets.ChangePasswordViewSet, basename='change_password')
urlpatterns = router.urls