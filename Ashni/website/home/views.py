from urllib import request
from django.shortcuts import render, redirect
from datetime import date, datetime
from home.models import Contact

# Create your views here.
def index(request):
    return render(request , 'index.html')

def stats(request):
    return render(request , 'stats.html')

def our_team(request):
    return render(request , 'our_team.html')

def about_us(request):
    return render(request , 'about_us.html')

def Awareness_session(request):
    return render(request, 'Awareness_session.html')

def Gender_sensitization(request):
    return render(request, 'Gender_sensitization.html')

def PoSH_awareness(request):
    return render(request, 'PoSH_awareness.html')

def contact_us(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone= request.POST.get('phone')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        contact_us = Contact(name=name, email=email, phone=phone, description=description,  date=datetime.today())
        contact_us.save()
        return render(request , 'response_submit.html')
    
    return render(request , 'contact_us.html')