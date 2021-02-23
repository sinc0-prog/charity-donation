from django.shortcuts import render
from django.views import View

class HomePageView(View):
    def get(self, request):
        return render(request, 'base.html')

class LoginPage(View):
    def get(self, request):
        return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
