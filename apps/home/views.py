from django.shortcuts import render, redirect
from django.views import View
from apps.home.forms import ContactForm
from django.contrib import messages
# Create your views here.

class HomePageView(View):
    def get(self, request):

     
        return render(request, 'home.html')
    
class ContactPage(View):
    def get(self, request):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('home:index')
        
        context = {
            'form': form
        }
        messages.error(request, f'Message not sent: {form.errors}')
        return render(request, 'contact.html', context)
    
    
class FormulaPage(View):
    def get(self, request):
        return render(request, 'formula.html')