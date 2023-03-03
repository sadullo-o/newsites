from django.urls import path
from .views import home, about, contact

urlpatterns = [
    path('', home, name='home'),  # yangi.uz
    path('about', about, name='about'),  # yangi.uz/about
    path('contact', contact, name='contact')
]