from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def available_cars(request):
    return render(request, "cars/cars.html")
