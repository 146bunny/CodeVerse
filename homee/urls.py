from django.urls import path
from . import views

urlpatterns = [

    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('search/', views.search,name='search'),
    path('logIn', views.handleLogIn,name='logIn'),
    path('logOut', views.handleLogOut,name='logOut'),
    path('signUp', views.handleSignUp,name='signUp'),
]
