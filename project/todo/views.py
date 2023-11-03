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
                return redirect('/register')
            else:
                creating_user= User.objects.create_user(username=username,
                                                        password=confirm_password)
                
                creating_user.save()
                auth.login(request, creating_user)
                messages.info(request, "Welcome to ToDo App")
                return redirect('/')

        else:
            messages.info(request, "Password did not match")
            return redirect('/register')

    def get(self, request):
        return render(request, 'register.html')




# Code for Sign in
class SignIn(View):
    def post(self, request):
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')

        user_login = auth.authenticate(username=username, password=password)

        if user_login is not None:
            auth.login(request, user_login)
            messages.info(request, 'Welcome back!')
            return redirect('/')
            
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('/login')

    def get(self, request):
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def home(request):
    return render(request, 'homepage.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')