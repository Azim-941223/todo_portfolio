from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('update/<int:pk>/', views.update_task, name='update'),
    path('complete/<int:pk>/', views.complete, name='complete'),
    path('un-complete/<int:pk>/', views.un_complete, name='un_complete'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('register/', views.sign_up, name='register'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
]