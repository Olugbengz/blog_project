from rest_framework import routers
from django.urls import path, include
from .views import BlogViewSet



router = routers.DefaultRouter()
router.register(r'', BlogViewSet)


urlpatterns = [
    path('', include(router.urls))
    ]