from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage, name= 'logout'),
    path('home-item/<str:pk>/', views.homeitemPage, name='home-item'),
    path('add-item/<str:pk>/', views.additemPage, name='add-item'),
]