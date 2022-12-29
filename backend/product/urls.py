from rest_framework.routers import DefaultRouter
from .views import ProductViewSet


router = DefaultRouter()
router.register(r'', ProductViewSet, basename='products')

urlpatterns = []
urlpatterns += router.urls
