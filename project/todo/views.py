from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import View
from django.contrib import messages
from todo.models import Task
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponseRedirect


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


# Code for Homepage 
class HomePage(LoginRequiredMixin, View):  # Inherit from LoginRequiredMixin
    login_url = '/login/'  # Set the login URL

    def post(self, request):
        try:
            task_text = request.POST.get('todo_text')
            if not task_text:
                messages.error(request, 'Task text cannot be empty.')
                return redirect('/')

            current_user = request.user
            task = Task(
                user=current_user,
                task=task_text,
            )
            task.save()

            messages.success(request, 'Task created successfully.')
            return redirect('/')

        except Exception as e:
            print(e)
            messages.error(request, 'Error creating task: {}'.format(e))
            return redirect('/')


    def get(self, request):
        return render(request, 'homepage.html')


# def home(request):
#     return render(request, 'homepage.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')