from rest_framework.serializers import ModelSerializer
from user.models import Profile
from feed.models import Feed


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

 