from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('home',views.home, name='home'),
    path('about',views.about, name = 'about'),
    path('destinations', views.destinations, name = 'destinations'),
    path('blogs', views.blogs, name = 'blogs'),
    path('contact', views.contact, name = 'contact'),
    path('discounts', views.discounts, name = 'discounts'),
    path('booking', views.booking, name = 'booking')


]