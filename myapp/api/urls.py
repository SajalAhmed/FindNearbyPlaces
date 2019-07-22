from rest_framework import routers
from myapp.api.views import LocationViewSet

router = routers.DefaultRouter()
router.register('location', LocationViewSet, base_name='place')
urlpatterns = router.urls