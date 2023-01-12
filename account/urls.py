from rest_framework.routers import DefaultRouter
from account.viewsets import RegisterViewSet
# from core.views import ScholarityViewSet, PostViewSet, FunctionViewSet, DepartamentViewSet, BondViewSet, EmployeeViewSet, AllocationViewSet, RelationAllocationFunctionViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'register', RegisterViewSet)
urlpatterns = router.urls