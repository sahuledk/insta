from django.shortcuts import render, redirect
from .models import Feed
from user.models import Profile
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FeedForm


# Create your views here.


class FeedCreate(CreateView):
    model = Feed
    fields = ['photo', 'status', 'owner']
    success_url = reverse_lazy('feed')

    # def get_form_kwargs(self):
    #     kwargs = super(FeedCreate, self).get_form_kwargs()
    #     kwargs['owner'] = self.request.user.profile
    #     return kwargs
    #
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.owner = self.request.user
    #     return super(FeedCreate, self).form_valid(form)


class FeedUpdate(LoginRequiredMixin, UpdateView):
    model = Feed
    fields = ['photo', 'status']
    success_url = reverse_lazy('Feed')


class FeedDelete(LoginRequiredMixin, DeleteView):
    model = Feed
    success_url = reverse_lazy('feed')


class Feeds(LoginRequiredMixin, ListView):
    model = Feed
    context_object_name = 'feeds'
    template_name = 'feed/feed.html'
    queryset = Feed.objects.all()

    def get_queryset(self):
        queryset = Feed.objects.exclude(owner=self.request.user.profile)
        return queryset





