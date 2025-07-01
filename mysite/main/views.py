from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')


def home(request):
    return render(request, 'main/home.html')

def projects(request):
    return render(request, 'main/projects.html')