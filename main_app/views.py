from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish, Toy
from .forms import FeedingForm
from django.views.generic import ListView, DetailView

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
  feeding_form = FeedingForm()
  return render(request, 'fishes/detail.html', { 'fish': fish, 'feeding_form': feeding_form })

def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('fish-detail', fish_id=fish_id)

class FishCreate(CreateView):
  model = Fish
  fields = ['name', 'breed', 'age', 'description']  
  # success_url = '/fishes/' --> I don't think I need this.

class FishUpdate(UpdateView):
  model = Fish
  fields = ['breed', 'description', 'age']

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fishes/'

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'