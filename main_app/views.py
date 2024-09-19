from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def fish_index(request):
  fishes = Fish.objects.all()
  return render(request, 'fishes/index.html', { 'fishes': fishes })

def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  return render(request, 'fishes/detail.html', { 'fish': fish })

class FishCreate(CreateView):
  model = Fish
  fields = '__all__'
  success_url = '/fishes/'

class FishUpdate(UpdateView):
  model = Fish
  fields = ['breed', 'description', 'age']

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fishes/'