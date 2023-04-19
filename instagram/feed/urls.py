from django.urls import path
from .views import Feeds, FeedCreate, FeedUpdate, FeedDelete

urlpatterns = [
    path('feed/', Feeds.as_view(), name='feed'),
    path('create/', FeedCreate.as_view(), name='feed-create'),
    path('update/<str:pk>/', FeedUpdate.as_view(), name='feed-update'),
    path('feed-delete/<str:pk>/', FeedDelete.as_view(), name='feed-delete')

]