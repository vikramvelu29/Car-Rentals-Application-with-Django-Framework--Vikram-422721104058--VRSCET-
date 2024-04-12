from django.urls import path
from . import views

app_name = 'aboutus'

urlpatterns = [
    path('', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    
    # Add more URL patterns as needed
]
