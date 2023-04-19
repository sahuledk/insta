from django.urls import path
from .views import CustomLogin, Register, UserProfile, UpdateProfile, DeleteProfile, Account
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('user-profile/<str:pk>/', UserProfile.as_view(), name='profile'),
    path('profile/<str:pk>/', UserProfile.as_view(), name='account'),
    path('update-profile/<str:pk>', UpdateProfile.as_view(), name='update-profile'),
    path('delete-profile/<str:pk>', DeleteProfile.as_view(), name='delete-profile'),
    path('account/<str:pk>', Account.as_view(), name='account'),

]