from django.shortcuts import render, HttpResponse, redirect
from .models import Yangilik, Trend, Aboutus, Blog, AboutLN
from .forms import ContactForm

# Create your views here.

def home(request):
    yangiliklar = Yangilik.objects.all()
    trends = Trend.objects.all()
    blogs1 = Blog.objects.all()[:3]
    blogs2 = Blog.objects.all()[3:]

    context = {
        'news': yangiliklar,
        'trends': trends,
        'blogs1': blogs1,
        'blogs2': blogs2
    }

    return render(request, 'main/index.html', context)

def about(request):
    aboutitems = Aboutus.objects.all()
    aboutln = AboutLN.objects.first()

    context = {
        'items': aboutitems,
        'aboutln': aboutln
    }
    return render(request, 'main/about.html', context)

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')


    return render(request, 'main/contact.html')



def category(request):
    return render(request, 'main/category.html')


def search(request):
    return render(request, 'main/search-result.html')


def singlepost(request, pk):
    blogs = Blog.objects.all()
    oneblog = Blog.objects.get(pk=pk)
    context = {
        'oneblog': oneblog,
        'blogs': blogs
    }

    return render(request, 'main/single-post.html', context)












