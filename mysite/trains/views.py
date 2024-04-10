from django.shortcuts import render
from django.http import HttpResponse
from trains.models import Train

# Create your views here.

def index(request):
    trains = Train.objects.all()
    return render(request, 'index.html', {'train_list': trains})
