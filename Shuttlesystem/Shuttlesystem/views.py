from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def booking(request):
    return render(request, 'booking.html')

def operator(request):
    return render(request, 'operator.html')

def about(request):
    return render(request, 'about.html')

def admin(request):
    return render(request, 'admin.html')

