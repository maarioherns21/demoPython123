from django.shortcuts import render
from .models import Cat, Dog
# Create your views here.
# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Define the home view

class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats/'

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

class CatUpdate(UpdateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats/'

class Dogcreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/'

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

class DogUpdate(UpdateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/'

def home(request):
  return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {'cats': cats})


def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', {'cat': cat})


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog })
