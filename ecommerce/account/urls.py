from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),

    path('email_verification/<str:uidb64>/<str:token>/', views.email_verification, name='email_verification'),
    path('email_verification_sent', views.email_verification_sent, name='email_verification_sent'),
    path('email_verification_success', views.email_verification_success, name='email_verification_success'),
    path('email_verification_failed', views.email_verification_failed, name='email_verification_failed'),

    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('profile_manage', views.profile_manage, name='profile_manage'),
    path('account_delete', views.account_delete, name='account_delete'),
]