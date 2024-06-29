from django.shortcuts import render, redirect
from django.views import View
from apps.accounts.models import User

# Create your views here.

class HomePageView(View):
    def get(self, request):

     
        return render(request, 'home.html')
    