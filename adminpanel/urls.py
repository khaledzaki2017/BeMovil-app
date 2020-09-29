from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet, base_name='users')
app_name = 'adminpanel'

urlpatterns = [
    path('', include(router.urls)),
]
