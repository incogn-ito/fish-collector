from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for fish index
  path('fishes/', views.fish_index, name='fish-index'),
  path('fishes/<int:fish_id>/', views.fish_detail, name='fish-detail'),
  path('fishes/create/', views.FishCreate.as_view(), name='fish-create'),
  path('fishes/<int:pk>/update/', views.FishUpdate.as_view(), name='fish-update'),
  path('fishes/<int:pk>/delete/', views.FishDelete.as_view(), name='fish-delete'),
  path('fishes/<int:fish_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('fishes/<int:fish_id>/assoc-toy/<int:toy_id>/', views.assoc_toy, name='assoc-toy'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
]