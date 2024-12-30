from django.urls import path, include
from . import views  # Import the views module

urlpatterns = [
    path('home/' , views.home, name='home'),
    path('customers/' , views.customer, name='customer'),
    path('' , views.layout , name='layout'),
    path('contact/' , views.contact, name='contact'),
    path('login/', views.login ,    name='login'),
    path('products/', views.products , name='products'),

]