from django.shortcuts import render

def home(request):
    return render(request, 'portfoilo/home.html')

def about(request):
    return render(request, 'portfoilo/about.html')
