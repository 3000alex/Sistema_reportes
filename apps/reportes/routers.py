from rest_framework.routers import DefaultRouter

from .import viewsets

router = DefaultRouter()
router.register(r'modelo1Prueba', viewsets.modelo1Prueba, basename="modelo1Prueba")

urlpatterns = router.urls