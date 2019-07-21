from rest_framework import routers
from myapp.api.views import TaskViewSet

router = routers.DefaultRouter()
router.register('location', TaskViewSet, base_name='tasks')
urlpatterns = router.urls