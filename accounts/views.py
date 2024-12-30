from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Home_page')

def customer(request):
    return HttpResponse('Customer_page')

def layout(request):
    return render(request, 'accounts/layout.html')


def contact(request):
    return render(request, 'accounts/contact.html')

def login(request):
    
    return render(request, 'accounts/login.html')

def products(request):
    unitprice = 2000
    q = 1000
    total = unitprice * q
    context = {
        'price': 2000,
        'totalPrice': total 
    }
    return render(request, 'accounts/product.html', context)


