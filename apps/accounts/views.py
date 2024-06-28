from django.shortcuts import render, redirect
from django.contrib import messages
from apps.accounts.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View
from apps.accounts.forms import UserRegisterForm, LoginForm, UpdateUserForm


# Create your views here.

class UserRegisterView(View):
    form_class = UserRegisterForm
    def get(self, request):
        form = self.form_class()
        context = {
            'form':form
        }
        return render(request, 'accounts/register.html', context)
    
    def post(self, request):
        user_form = self.form_class(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "tizimdan muvaffaqiyatli ro'yxatdan o'tdingiz...")
            return redirect("accounts:login")
            

        messages.error(request, "Tizimdan ro'yxatdan o'ta olmadingiz...")
        context ={
            "form":user_form,
        }
        return render(request, 'accounts/register.html', context)
    

class LoginView(View):
    form_class = LoginForm
    def get(self, request):
        form = self.form_class()
        context={
            'form':form
        } 
        return render(request, 'accounts/login.html', context)
    
    def post(self, request):
        user_form = self.form_class(data = request.POST)
        if user_form.is_valid():
            user = authenticate(request, email = user_form.cleaned_data['email'], password = user_form.cleaned_data['password'])
            if user is not None:
                print(user)
                login(request, user)
                messages.success(request, 'Siz tizimga muvaffaqiyatli kirdingiz...')
                return redirect("home:index")

            messages.error(request, "Login yoki parol noto'g'ri!!!")
            return render(request, "accounts/login.html", {'form': user_form})
        

        messages.error(request, user_form.errors)
        return render(request, "accounts/login.html", {'form': user_form})

class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home:index')

class UpdateUserView(View):
    form_class = UpdateUserForm
    def get(self , request):
        form = self.form_class(instance=request.user)
        context ={
            'form':form
        }
        return render(request, 'accounts/update.html', context )
    def post(self, request):
        user_form = self.form_class(data=request.POST, files=request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Muvaffaqiyatli yangilandi...')
            return redirect('home:index')
        
        messages.error(request, user_form.errors)
        return render(request, 'accounts/update.html', {'form':user_form})
    




