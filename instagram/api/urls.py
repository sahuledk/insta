from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )

router = DefaultRouter()
router.register(r'view', views.ProfileViewset, basename='view')
router.register(r'uploads', views.FeedViewset, basename='uploads')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



]

urlpatterns += router.urls

