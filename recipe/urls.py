from django.urls import path
from .views import ListRecipes, CreateRecipe, DetailRecipe, UpdateRecipe, DeleteRecipe
urlpatterns = [
   path('', ListRecipes.as_view(), name='recipes'),
   path('new/', CreateRecipe.as_view(), name='create_recipe'),
   path('<int:pk>/', DetailRecipe.as_view(), name='recipe_detail'),
   path('<int:pk>/update/', UpdateRecipe.as_view(), name='recipe_update'),
   path('<int:pk>/delete/', DeleteRecipe.as_view(), name='recipe_delete')
]