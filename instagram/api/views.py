from django.shortcuts import render
from feed.models import Feed
from user.models import Profile
from rest_framework import viewsets
from .serializers import ProfileSerializer, FeedSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer


class FeedViewset(viewsets.ModelViewSet):

    queryset = Feed.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FeedSerializer

# class ProfileList(generics.ListCreateAPIView):
#
