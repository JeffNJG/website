from django.shortcuts import render, redirect
from django.views import View


class HomeView(View):
    """This is the view for Home page"""
    
    def get(self, request, *args, **kwargs):
        return render(self.request, "base/index.html")


class SignupView(View):
    """This is the view for signup"""
    
    def get(self, request, *args, **kwargs):
        return render(self.request, "base/signup.html")
