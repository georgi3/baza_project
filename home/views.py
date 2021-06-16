from django.shortcuts import render
# from .models import Fishing
# from .models import Mushrooms
# from .models import Events


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/aboutus.html')


def activities(request):
    return render(request, 'home/activities.html')
