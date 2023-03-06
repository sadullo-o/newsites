from django.shortcuts import render, HttpResponse
from .models import Yangilik, Trend, Aboutus

# Create your views here.

def home(request):
    yangiliklar = Yangilik.objects.all()
    trends = Trend.objects.all()

    context = {
        'news': yangiliklar,
        'trends': trends
    }

    return render(request, 'main/index.html', context)

def about(request):
    aboutitems = Aboutus.objects.all()

    context = {
        'items': aboutitems
    }
    return render(request, 'main/about.html', context)

def contact(request):
    return render(request, 'main/contact.html')



def category(request):
    return render(request, 'main/category.html')


def search(request):
    return render(request, 'main/search-result.html')


def singlepost(request):
    return render(request, 'main/single-post.html')












