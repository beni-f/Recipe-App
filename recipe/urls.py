from django.urls import path
from .views import ListRecipes, CreateRecipe
urlpatterns = [
   path('', ListRecipes.as_view(), name='recipes'),
   path('new/', CreateRecipe.as_view(), name='create_recipe')
]