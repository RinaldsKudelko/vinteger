from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    
    return render(request, 'home/home.html')

def about(request):
    
    return HttpResponse('home/about.html')
# Create your views here.
