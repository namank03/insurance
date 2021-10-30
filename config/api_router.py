from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from insurance.base.api.views import CustomerViewSet, PolicyViewSet
from insurance.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("policies", PolicyViewSet)
router.register("customers", CustomerViewSet)


app_name = "api"
urlpatterns = router.urls
