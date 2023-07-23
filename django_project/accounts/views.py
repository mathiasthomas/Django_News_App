from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserCreationForm
from django.views.generic import CreateView


# ----------Signup View ---------

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
