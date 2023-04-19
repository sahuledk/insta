from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
from .models import Feed
from django.contrib.auth.models import User

class FeedForm(ModelForm):
    model = Feed
    fields = ['photo', 'status', 'owner']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(FeedForm, self).__init__(*args, **kwargs)
        self.fields['owner'].queryset = Feed.objects.filter(user=user)

