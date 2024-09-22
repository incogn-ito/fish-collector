from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Fish, Toy
from .forms import FeedingForm
from .forms import FishForm

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def fish_index(request):
  # fishes = Fish.objects.all()
  fishes = Fish.objects.filter(user=request.user)
  return render(request, 'fishes/index.html', { 'fishes': fishes })

@login_required
def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  # Get the toys the fish doesn't have
  toys_fish_doesnt_have = Toy.objects.exclude(id__in = fish.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'fishes/detail.html', {
    # Add the toys to be displayed
    'fish': fish, 'feeding_form': feeding_form, 'toys': toys_fish_doesnt_have
  })

@login_required
def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('fish-detail', fish_id=fish_id)

@login_required
def assoc_toy(request, fish_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Fish.objects.get(id=fish_id).toys.add(toy_id)
  return redirect('fish-detail', fish_id=fish_id)

class FishCreate(LoginRequiredMixin, CreateView):
    model = Fish
    form_class = FishForm  # Use the form with image selection
    template_name = 'fishes/fish_form.html'
    success_url = reverse_lazy('fish-index')
    
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
      form.instance.user = self.request.user  
    # form.instance is the fish
    # Let the CreateView do its job as usual
      return super().form_valid(form)

class FishUpdate(LoginRequiredMixin, UpdateView):
    model = Fish
    form_class = FishForm  # Use the same form for updating
    template_name = 'fishes/fish_form.html'
    success_url = reverse_lazy('fish-index')

class FishDelete(LoginRequiredMixin, DeleteView):
  model = Fish
  success_url = '/fishes/'

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('fish-index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})