from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/create/', views.Dogcreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),

]
