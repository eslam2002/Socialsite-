from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView,)
# reverse_lazy is used in case some one is logged in or logged and U wanna to send them some where
from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'