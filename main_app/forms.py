from django.forms import ModelForm
from .models import Feeding
from django import forms
from .models import Fish

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']

FISH_IMAGES = [
    ('images/Betta-fish.png', 'Betta fish'),
    ('images/Blue-tang-fish.png', 'Blue tang fish'),
    ('images/Clownfish.png', 'Clownfish'),
    ('images/default-fish.png', 'Default fish'),
    ('images/Goby-fish.png', 'Goby fish'),
    ('images/Goldfish.png', 'Goldfish'),
    ('images/Lionfish.png', 'Lionfish'),
    ('images/Puffer-fish.png', 'Puffer fish'),
    ('images/Rainbow-fish.png', 'Rainbow fish'),
    ('images/Red-snapper-fish.png', 'Red snapper fish'),
    ('images/Swordfish.png', 'Swordfish'),
    ('images/Trigger-fish.png', 'Trigger fish'),
    ('images/Wrasse-fish.png', 'Wrasse fish'),
]


class FishForm(forms.ModelForm):
    image_url = forms.ChoiceField(choices=FISH_IMAGES, label="Select an Image")

    class Meta:
        model = Fish
        fields = ['name', 'breed', 'age', 'description', 'image_url']