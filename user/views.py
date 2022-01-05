from django.shortcuts import render, redirect

from product import models
from . models import post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login


from django.urls import reverse_lazy


class RegisterPage(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('post')
        return super(RegisterPage, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('post')


class PostList(LoginRequiredMixin, ListView):
    model = post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = context['post'].filter(user=self.request.user)
        return context


class PostDetail(LoginRequiredMixin, DetailView):
    model = post
    context_object_name = 'posts'


class PostCreate(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'text']
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = post
    fields = ['title', 'text']
    success_url = reverse_lazy('post')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = post
    context_object_name = 'post'
    success_url = reverse_lazy('post')
