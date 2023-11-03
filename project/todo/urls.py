from django.urls import path
from . import views
from .views import home, login, SignUp, SignIn

urlpatterns=[
    path('', views.home, name='Home'),
    path('login/', SignIn.as_view(), name='Login'),
    path('register/', SignUp.as_view(), name='Register'),
    path('logout/', views.logout, name='Logout'),

    
]