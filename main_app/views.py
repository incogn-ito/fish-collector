from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .models import Fish, Toy
from .forms import FeedingForm

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

# Add new view
def fish_index(request):
  fishes = Fish.objects.all()
  return render(request, 'fishes/index.html', { 'fishes': fishes })

def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  # Get the toys the fish doesn't have
  toys_fish_doesnt_have = Toy.objects.exclude(id__in = fish.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'fishes/detail.html', {
    # Add the toys to be displayed
    'fish': fish, 'feeding_form': feeding_form, 'toys': toys_fish_doesnt_have
  })

def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('fish-detail', fish_id=fish_id)

def assoc_toy(request, fish_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Fish.objects.get(id=fish_id).toys.add(toy_id)
  return redirect('fish-detail', fish_id=fish_id)

class FishCreate(CreateView):
  model = Fish
  fields = ['name', 'breed', 'age', 'description']
  
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  
    # form.instance is the fish
    # Let the CreateView do its job as usual
    return super().form_valid(form)

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