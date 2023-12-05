from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('product/<slug:slug>/', views.product_infor, name='product_infor'),
    path('category/<slug:slug>/', views.list_category, name='list_category'),
]