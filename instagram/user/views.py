from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Profile
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLogin(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('feed')


class Register(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('feed')
        return super(Register, self).get(*args, **kwargs)


class UserProfile(LoginRequiredMixin, DetailView):
    model = Profile
    fields = '__all__'


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = '__all__'
    template_name = 'user/profile.html'
    success_url = reverse_lazy('feed')


class DeleteProfile(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'user/delete.html'


class Account(LoginRequiredMixin, DetailView):
    model = Profile
    fields = '__all__'
    template_name = 'user/account.html'
