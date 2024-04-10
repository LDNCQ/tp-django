from django.shortcuts import render, redirect
from django.http import HttpResponse
from trains.models import Train
import random

# Create your views here.

def index(request):
    trains = Train.objects.all()
    return render(request, 'index.html', {'train_list': trains})

def detail_train(request, train_id):
    train = Train.objects.get(pk=train_id)
    context = {
        'train': train,
    }
    return render(request, 'detail_train.html', context)

def page_aleatoire(request):
    aleatoire = random.choice(Train.objects.all())
    return redirect('detail_train', train_id=aleatoire.id)