from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout')
]
