from django.shortcuts import render
from django.views import View
import random
from app.models import *

class HomePageView(View):
    def get(self, request):
        fundation = list(Institution.objects.filter(type_of = 'fundacja'))
        non_profit_org = list(Institution.objects.filter(type_of = 'organizacja pozarzadowa'))
        local_collection = list(Institution.objects.filter(type_of = 'zbiórka lokalna'))
        counter_fundation = len(fundation)
        counter_non_profit_org = len(non_profit_org)
        counter_local_collection = len(local_collection)
        try:
            random_fundation = random.sample(fundation, 3)
            random_non_profit_org = random.sample(non_profit_org, 4)
            random_local_collection = random.sample(local_collection, 2)
        except ValueError:
            random_fundation = random.sample(fundation, counter_fundation)
            random_non_profit_org = random.sample(non_profit_org, counter_non_profit_org)
            random_local_collection = random.sample(local_collection, counter_local_collection)
        return render(request, 'base.html', {'random_fundation': random_fundation, 
                                            'random_non_profit_org': random_non_profit_org, 
                                            'random_local_collection': random_local_collection})

class LoginPage(View):
    def get(self, request):
        return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
