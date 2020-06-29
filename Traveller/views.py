from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Destination
from django.contrib import messages
from django.contrib.auth.models import User,auth


def index(request):
   dests = Destination.objects.all()
   return render(request,'index.html', {'dests':dests})

def home(request):
   return render(request,'index.html')

def about(request):
   return render(request, 'about.html')

def destinations(request):
   return render(request, 'destination.html')

def blogs(request):
   if request.user.is_authenticated:
      return render(request, 'blog.html')
   else:
      messages.info(request, 'In order to access blogs')
      return redirect('/accounts/register')

def contact(request):
   return render(request, 'contact.html')

def discounts(request):
   dests = Destination.objects.all()
   return render(request, 'discount.html', {'dests':dests})

def booking(request):
   return render(request, 'booking.html')