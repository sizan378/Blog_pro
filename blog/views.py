from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import Post
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class DetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author','body']


class BlogUpadateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


