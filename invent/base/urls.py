from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage, name= 'logout'),
    path('register/', views.registerPage, name = 'register'),
    path('home-item/<str:pk>/', views.homeitemPage, name='home-item'),
    path('add-item/<str:pk>/', views.additemPage, name='add-item'),
    path('item-details/<str:pk>/', views.itemDetails, name='details'),
    path('update-item/<str:pk>/', views.updtateItem, name = 'update'),
    path('delete-item/<str:pk>/', views.deleteItem, name= 'delete'),
    path('add-home/', views.addHome, name = 'new-home'),
    path('update-home/<str:pk>/', views.updateHome, name = 'update-home'),
    path('delete-home/<str:pk>/', views.deleteHome, name='delete-home'),
]