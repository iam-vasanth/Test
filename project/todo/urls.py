from django.urls import path
from . import views
from .views import login, SignUp, SignIn, HomePage

urlpatterns=[
    path('', HomePage.as_view(), name='Home'),
    path('login/', SignIn.as_view(), name='Login'),
    path('register/', SignUp.as_view(), name='Register'),
    path('logout/', views.logout, name='Logout'),

    
]