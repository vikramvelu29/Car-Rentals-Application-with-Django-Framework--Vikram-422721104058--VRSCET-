from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def aboutus(request):
    return render(request, "aboutus/aboutus.html")
def contact(request):
    return render(request, "cars/Contact.html")
