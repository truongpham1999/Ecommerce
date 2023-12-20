from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    # Registration
    path('register', views.register, name='register'),

    # Email Verification
    path('email_verification/<str:uidb64>/<str:token>/', views.email_verification, name='email_verification'),
    path('email_verification_sent', views.email_verification_sent, name='email_verification_sent'),
    path('email_verification_success', views.email_verification_success, name='email_verification_success'),
    path('email_verification_failed', views.email_verification_failed, name='email_verification_failed'),

    # Login/Logout
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    # Dashboard
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile_manage', views.profile_manage, name='profile_manage'),
    path('account_delete', views.account_delete, name='account_delete'),

    # Password urls/views
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='account/password/password_reset.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='account/password/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='account/password/password_reset_complete.html'), name='password_reset_complete'),

    # Shipping Management
    path('manage_shipping', views.manage_shipping, name='manage_shipping'),

    # Order Management
    path('track_orders', views.track_orders, name='track_orders'),
]