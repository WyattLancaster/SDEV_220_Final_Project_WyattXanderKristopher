from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('register/', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout/', views.user_logout, name='lougout'),
]