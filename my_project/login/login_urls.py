from django.urls import path
from login import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login_result/', views.login_result, name='login_result')
]
