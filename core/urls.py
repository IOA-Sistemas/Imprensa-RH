from rest_framework.routers import DefaultRouter
from core.views import ScholarityViewSet, PostViewSet, FunctionViewSet, DepartamentViewSet, BondViewSet, EmployeeViewSet, AllocationViewSet, RelationAllocationFunctionViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'servidor', EmployeeViewSet)

urlpatterns = router.urls