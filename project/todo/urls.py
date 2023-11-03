from django.urls import path
from . import views
from .views import home, login, SignUp

urlpatterns=[
    path('', views.home, name='Home'),
#     path('login/', views.login, name='Login'),
    path('register/', SignUp.as_view(), name='Register'),
    
]