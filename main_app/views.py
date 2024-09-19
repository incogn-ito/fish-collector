from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Fish:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

fishes = [
  Fish('Lolo', 'swordfish', 'Kinda rude.', 3),
  Fish('Sachi', 'snapper', 'Looks a little red.', 0),
  Fish('Fancy', 'goldfish', 'Happy tail.', 4),
  Fish('Bonk', 'betta', 'Gurles loudly.', 6)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello <>< </h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def fish_index(request):
  return render(request, 'fishes/index.html', { 'fishes': fishes })


