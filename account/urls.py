from rest_framework.routers import DefaultRouter
from account.viewsets import RegisterViewSet, UpdateViewSet
# from core.views import ScholarityViewSet, PostViewSet, FunctionViewSet, DepartamentViewSet, BondViewSet, EmployeeViewSet, AllocationViewSet, RelationAllocationFunctionViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'register', RegisterViewSet)
router.register(r'update', UpdateViewSet)
urlpatterns = router.urls