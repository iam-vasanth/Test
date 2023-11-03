from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import View
from django.contrib import messages

#Code for Account Sing up
class SignUp(View):
    def post(self,request):
        username = request.POST.get('username_r')
        password = request.POST.get('password_r')
        confirm_password = request.POST.get('password_rc')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            else:
                creating_user= User.objects.create_user(username=username,
                                                        password=confirm_password)
                
                creating_user.save()
                messages.info(request, "Welcome to ToDO App")
                return redirect('/')

        else:
            messages.info(request, "Password did not match")
            return redirect('register')

    def get(self, request):
        return render(request, 'register.html')


def home(request):
    return render(request, 'homepage.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')