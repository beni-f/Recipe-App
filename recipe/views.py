from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Recipe


class ListRecipes(ListView):
    """
        List all recpies available.
    """
    model = Recipe
    template_name = 'recipe_list.html'

class CreateRecipe(CreateView):
    """
        Creates a recpie
    """
    model = Recipe
    fields = ('__all__')
    template_name = 'create_recpie.html'

class DetailRecipe(DetailView):
    """
        Displays the details for a recipe
    """
    model = Recipe
    template_name = 'recipe_detail.html'

class UpdateRecipe(UpdateView):
    """
        Updates a Recipe
    """
    model = Recipe
    fields = ('__all__')
    template_name = 'recipe_update.html'

class DeleteRecipe(DeleteView):
    model = Recipe
    success_url = 'recipes'
    template_name = 'recipe_delete.html'
