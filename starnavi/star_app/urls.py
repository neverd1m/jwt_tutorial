from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views


router = routers.DefaultRouter()

router.register(r'user', views.UserViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'profile', views.ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
