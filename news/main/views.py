from django.shortcuts import render, HttpResponse
from .models import Yangilik

# Create your views here.

def home(request):
    yangiliklar = Yangilik.objects.all()

    context = {
        'news': yangiliklar
    }

    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')