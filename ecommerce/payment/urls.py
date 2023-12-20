from django.urls import path
from . import views

urlpatterns = [
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete_checkout/', views.complete_checkout, name='complete_checkout'),
]